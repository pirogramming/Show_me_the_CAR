from django.db import models
from core import models as core_models


class Brand(core_models.TimeStampedModel):

    """ Brand Model Definition """

    name = models.CharField(max_length=80)
    homepage = models.URLField(max_length=240)

    def __str__(self):
        return self.name


class Car(core_models.TimeStampedModel):

    """ Car Model Definition """

    model_name = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    url = models.URLField(max_length=250)
    brand = models.ForeignKey("Brand", on_delete=models.SET_NULL, related_name="cars")
    shop = models.ManyToManyField("shops.Shop", related_name="cars", blank=True)

