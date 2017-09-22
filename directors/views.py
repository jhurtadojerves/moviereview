from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Director

# Create your views here.


class DirectorList(ListView):
    model = Director
    context_object_name = 'directors'


class DirectorDetail(DetailView):
    model = Director
    context_object_name = 'director'
