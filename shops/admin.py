from django.contrib import admin
from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    """ Shop Admin Definition """

    list_display = [
        "name",
        "get_cars",
    ]
    list_display_links = [
        "name",
    ]

    def get_cars(self, obj):
        return "\n".join([car.cars for car in self.car.all()])


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):

    pass

