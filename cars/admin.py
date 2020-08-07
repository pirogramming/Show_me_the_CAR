from django.contrib import admin
from . import models

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):

    """ Car Admin Definition """

    pass


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):

    """ Brand Admin Definition"""

    pass
