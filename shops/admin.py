from django.contrib import admin
from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    """ Shop Admin Definition """

    list_display = [
        "name",
        "phone_number",
        "city",
        "region",
        "count_cars",
    ]

    list_filter = [
        "name",
        "phone_number",
        "city",
        "region",
    ]

    search_fields = (
        "^name",
        "^phone_number",
        "^city",
        "^region",
    )

    def count_cars(self, obj):
        return obj.cars.count()

    count_cars.short_description = "Number of Cars"


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):

    pass

