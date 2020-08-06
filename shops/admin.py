from django.contrib import admin
from . import models


@admin.register(models.Rating, models.Favorite)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    """ Shop Admin Definition """

    pass
