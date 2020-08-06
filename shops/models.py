from django.db import models
from core import models as core_models
from users.models import User


class Rating(core_models.TimeStampedModel):
    """ Rating Model Definition """

    pass


class Shop(core_models.TimeStampedModel):
    """ Shop Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    region = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    homepage = models.URLField(max_length=250)
    phone_number = models.IntegerField()

    # favorite, star
    favorite = models.ManyToManyField(User)

    def __str__(self):
        return self.name
