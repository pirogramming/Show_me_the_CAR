from django import forms
from . import models


class SearchForm(forms.Form):

    """ Search Form Definition """

    OPTIONS = [
        ('', '지역'),
        ('서울특별시', '서울특별시'),
        ('부산광역시', '부산광역시'),
        ('대구광역시', '대구광역시'),
        ('인천광역시', '인천광역시'),
        ('광주광역시', '광주광역시'),
        ('대전광역시', '대전광역시'),
        ('울산광역시', '울산광역시'),
        ('세종특별자치시', '세종특별자치시'),
        ('경기도', '경기도'),
        ('강원도', '강원도'),
        ('충청북도', '충청북도'),
        ('충청남도', '충청남도'),
        ('전라북도', '전라북도'),
        ('전라남도', '전라남도'),
        ('경상북도', '경상북도'),
        ('경상남도', '경상남도'),
        ('제주특별자치시도', '제주특별자치시도'),
    ]

    city = forms.ChoiceField(initial="Anywhere", required=False, label="", choices=OPTIONS)
    car_model = forms.CharField(label="",
                                widget=forms.TextInput(attrs={'placeholder': '자동차 모델명'}))


# class RatingForm(forms.Form):
#     rating = forms.IntegerField(required=False)

