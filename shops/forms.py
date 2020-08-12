from django import forms
from . import models


class SearchForm(forms.Form):

    """ Search Form Definition """

    # city = forms.CharField(initial="Anywhere", required=False, label="도시")
    car_model = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'placeholder': '모델 검색'}))


# class RatingForm(forms.Form):
#     rating = forms.IntegerField(required=False)

