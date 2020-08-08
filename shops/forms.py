from django import forms
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    car = forms.ModelChoiceField(queryset=models.Car.object.all())
