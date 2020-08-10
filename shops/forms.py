from django import forms
from . import models


class SearchForm(forms.Form):

    """ Search Form Definition """

    # city = forms.CharField(initial="Anywhere", required=False, label="도시")
    car_model = forms.CharField(label="차 모델")


class RatingForm(forms.Form):
    rating = forms.IntegerField(required=False)

