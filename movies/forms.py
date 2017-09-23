from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Movie, Review


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

class ReviewCreateForm(ModelForm):
    class Meta:
        model = Review
        fields = {'rating', 'comment', }
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5', }),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
