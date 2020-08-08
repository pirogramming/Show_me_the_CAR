from django.db import models
from core import models as core_models
from users.models import *


class Shop(core_models.TimeStampedModel):
    """ Shop Model Definition """

    name = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=80, blank=True)
    homepage = models.URLField(max_length=250, blank=True)
    phone_number = models.IntegerField(blank=True) # phone_number 모델 추후 수정 필요
    average = models.IntegerField(blank=True)
    like_users = models.ManyToManyField(User, related_name='like_shops')

    def __str__(self):
        return self.name


class Rating(core_models.TimeStampedModel):

    """ Rating Model Definition """

    user = models.ManyToManyField(User, related_name="ratings")
    shop = models.ForeignKey(
        Shop, related_name="shops_rating", on_delete=models.CASCADE
    )
    rating = models.SmallIntegerField(blank=True)

