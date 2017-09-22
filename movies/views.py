from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Movie

# Create your views here.


class MovieList(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'
