from django.db import models
from core import models as core_models
from users.models import User

from users.models import *



class Shop(core_models.TimeStampedModel):
    """ Shop Model Definition """

    name = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=80, blank=True)
    homepage = models.URLField(max_length=250, blank=True)
    phone_number = models.IntegerField(blank=True)
    like_users = models.ManyToManyField(User, related_name='like_posts')



    def __str__(self):
        return self.name



