from django.contrib import admin
from . import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    list_display = [
        "model_name",
        "color",
        "count_shops",
    ]
    list_filter = [
        "model_name",
        "color",
        "shop",
    ]

    search_fields = (
        "^model_name",
        "^color",
        "^shop__name",
    )

    def count_shops(self, obj):
        return obj.shop.count()

    count_shops.short_description = "Number of Shops"


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):

    """ Brand Admin Definition"""

    list_display = [
        "name",
        "count_cars",
    ]

    def count_cars(self, obj):
        return obj.cars.count()

    count_cars.short_description = "Number of Cars"
