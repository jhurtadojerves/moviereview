from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .forms import UpdateForm, CreateForm

from .models import Movie
from userprofiles.models import Profile

# Create your views here.

class MovieCreate(CreateView):
    model = Movie
    form_class = CreateForm
    template_name_suffix = '_form_create'

    def form_valid(self, form):
        #form.instance.cover = self.get_form_kwargs().get('files')['cover']
        form.instance.author = Profile.objects.get(user=self.request.user)
        movie = form.save()
        #return redirect('Movie:list')

        return HttpResponseRedirect(reverse('Movie:detail', args=(movie.slug,)))

class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'


class MovieUpdate(UpdateView):
    model = Movie
    form_class = UpdateForm

    def get_success_url(self):
        return reverse_lazy('Movie:detail', args=(self.object.slug,))

