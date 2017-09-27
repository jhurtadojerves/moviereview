from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, RedirectView

from .forms import SignInForm, SignUpForm, UpdateProfileForm

from .models import Profile

# Create your views here.


class DetailProfile(DetailView):
    model = Profile
    context_object_name = 'profile'
    slug_field = 'user__username'


class SignUpView(CreateView):
    model = Profile
    form_class = SignUpForm
    template_name_suffix = '_create'

    def form_valid(self, form):
        profile = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('Profile:detail', args=(user.username, )))


class SignInView(LoginView):
    template_name = 'userprofiles/login.html'
    authentication_form = SignInForm

    def get_success_url(self):
        profile = Profile.objects.get(user=self.request.user)
        return reverse('Profile:detail', args=(profile.user.username, ))


class SignOutView(RedirectView):
    url = reverse_lazy('Movie:list')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class UpdateProfile(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name_suffix = '_update'

    def get_object(self, queryset=None):
        queryset = Profile.objects.get(user=self.request.user)
        return queryset

    def get_success_url(self):
        profile = Profile.objects.get(user=self.request.user)
        return reverse('Profile:detail', args=(profile.user.username, ))
