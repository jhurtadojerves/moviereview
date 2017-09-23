from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Director


class CreateForm(ModelForm):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name', 'bio', 'birthday', )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
