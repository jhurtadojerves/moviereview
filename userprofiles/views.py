from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Profile

# Create your views here.


class DetailProfile(DetailView):
    model = Profile
    context_object_name = 'profile'
    slug_field = 'user__username'

