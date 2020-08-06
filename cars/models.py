from django.db import models
from core import models as core_models


class Car(core_models.TimeStampedModel):

    """ Car Model Definition """

    model_name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    homepage = models.URLField(max_length=250)
    shop = models.ManyToManyField("shops.Shop", related_name="cars", blank=True)

