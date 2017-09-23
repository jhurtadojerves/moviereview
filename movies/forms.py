from django import forms
from django.forms import ModelForm

from .models import Movie


class UpdateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'synopsis', 'director',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'synopsis', 'director', 'cover', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
        }
