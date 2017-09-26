from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .forms import UpdateForm, CreateForm, ReviewCreateForm

from .models import Movie, Review
from userprofiles.models import Profile

# Create your views here.


@method_decorator(login_required, name='dispatch')
class MovieCreate(CreateView):
    model = Movie
    form_class = CreateForm
    template_name_suffix = '_form_create'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        movie = form.save()

        return HttpResponseRedirect(reverse('Movie:detail', args=(movie.slug,)))


class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        movie = Movie.objects.get(slug=self.kwargs['slug'])

        if Review.objects.filter(user=profile, movie=movie).exists():
            context['created_comment'] = True
        return context


@method_decorator(login_required, name='dispatch')
class MovieUpdate(UpdateView):
    model = Movie
    form_class = UpdateForm

    def get_success_url(self):
        return reverse_lazy('Movie:detail', args=(self.object.slug,))


@method_decorator(login_required, name='dispatch')
class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name_suffix = '_create'

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        movie = Movie.objects.get(slug=self.kwargs['slug'])
        if Review.objects.filter(user=profile, movie=movie).exists():
            return HttpResponseRedirect(reverse('Movie:review_update', args=(movie.slug,)))
        else:
            return super(ReviewCreate, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user=self.request.user)
        movie = Movie.objects.get(slug=self.kwargs['slug'])
        form.instance.movie = movie
        form.save()

        return HttpResponseRedirect(reverse('Movie:detail', args=(movie.slug,)))


@method_decorator(login_required, name='dispatch')
class ReviewUpdate(UpdateView):
    model = Review
    form_class = ReviewCreateForm
    template_name_suffix = '_update'

    def get_object(self, queryset=None):
        queryset = Review.objects.get(user__user=self.request.user, movie=Movie.objects.get(slug=self.kwargs['slug']))
        return queryset

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        movie = Movie.objects.get(slug=self.kwargs['slug'])
        if not Review.objects.filter(user=profile, movie=movie).exists():
            return HttpResponseRedirect(reverse('Movie:review_create', args=(movie.slug,)))
        else:
            return super(ReviewUpdate, self).get(request, *args, **kwargs)

    def get_success_url(self):
        movie = Movie.objects.get(slug=self.kwargs['slug'])
        return reverse('Movie:detail', args=(movie.slug,))
