from django import forms
from django.forms import ModelForm

from .models import Movie


class UpdateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'review', 'director',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'review', 'director', 'cover', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
        }
