from django.contrib import admin
from . import models
from users.forms import RatingForm


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    """ Shop Admin Definition """

    list_display = [
        "name",
        "phone_number",
        "city",
        "region",
        "address",
        "count_cars",
        "get_average_rating",
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

    """ Rating Admin Definition """

    list_display = (
        "user",
        "shop",
        "rating",
    )

    form = RatingForm


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
