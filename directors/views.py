from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .forms import CreateForm

from .models import Director

# Create your views here.


class DirectorList(ListView):
    model = Director
    context_object_name = 'directors'


class DirectorDetail(DetailView):
    model = Director
    context_object_name = 'director'


@method_decorator(login_required, name='dispatch')
class DirectorCreate(CreateView):
    model = Director
    form_class = CreateForm
    template_name_suffix = '_create'

