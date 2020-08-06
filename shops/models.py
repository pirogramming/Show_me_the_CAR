from django.db import models
from core import models as core_models

from users.models import *


class Rating(core_models.TimeStampedModel):

    """ Rating Model Definition """

    pass


class Shop(core_models.TimeStampedModel):

    """ Shop Model Definition """

    name = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=80, blank=True)
    homepage = models.URLField(max_length=250, blank=True)
    phone_number = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Favorite(core_models.TimeStampedModel):

    """ Favorite Model Definition"""

    user = models.ManyToManyField(User, related_name='favorites')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
