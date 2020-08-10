from django.db import models
from django.urls import reverse
from core import models as core_models


class Shop(core_models.TimeStampedModel):
    """ Shop Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField(null=True)
    region = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    homepage = models.URLField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=80, blank=True, null=True)
    average = models.IntegerField(blank=True, null=True)
    like_users = models.ManyToManyField(
        "users.User", related_name="like_shops", blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:shop_detail", kwargs={"pk": self.pk})


class Rating(core_models.TimeStampedModel):

    """ Rating Model Definition """

    user = models.ManyToManyField("users.User", related_name="ratings")
    shop = models.ForeignKey(
        Shop, related_name="shops_rating", on_delete=models.CASCADE
    )
    rating = models.SmallIntegerField(blank=True)

