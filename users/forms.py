from django import forms
from shops.models import Rating
from .widgets import RateShopWidget


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["rating"]
        widgets = {
            "rating": RateShopWidget,
        }
        labels = {
            "rating": "",
        }

