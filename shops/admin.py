from django.contrib import admin
from . import models
from users.forms import RatingForm

@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    """ Shop Admin Definition """

    list_display = [
        "name",
    ]
    list_display_links = [
        "name",
    ]


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    form = RatingForm

