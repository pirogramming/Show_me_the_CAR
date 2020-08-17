from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
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
    average = models.FloatField(blank=True, null=True, default=None)
    like_users = models.ManyToManyField(
        "users.User", related_name="like_shops", blank=True, through="Rating"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shops:shop_detail", kwargs={"pk": self.pk})

    def get_average_rating(self):
        ratings = self.ratings.all()
        sum_rating = 0
        number_of_ratings = 0
        for rating in ratings:
            if rating.rating is None:
                continue
            sum_rating += int(rating.rating)
            number_of_ratings += 1
        try:
            avg_rating = round((sum_rating / number_of_ratings), 2)
        except ZeroDivisionError:
            avg_rating = 0
        return avg_rating

    get_average_rating.short_description = "Avg. rating"

    def save(self, *args, **kwargs):
        self.average = self.get_average_rating()
        super(Shop, self).save(*args, **kwargs)  # Call the real save() method


class Rating(core_models.TimeStampedModel):

    """ Rating Model Definition """

    user = models.ForeignKey(
        "users.User", related_name="ratings", on_delete=models.CASCADE, null=True
    )
    shop = models.ForeignKey(
        "shops.Shop", related_name="ratings", on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        blank=True,
        default=None,
    )

    def __str__(self):
        return str(self.rating)


class Comment(core_models.TimeStampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, verbose_name='comment')

