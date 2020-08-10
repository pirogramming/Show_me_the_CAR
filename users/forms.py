from django import forms
from shops.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        labels = {
            'rating': '별점',
        }