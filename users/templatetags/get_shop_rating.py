from django import template
from users.models import User as user_models
from shops.models import Shop as shop_models
from shops.models import Rating as rating_models

register = template.Library()


@register.filter
def get_shop_rating(shop_ratings, user):
    # print(shop_ratings)
    # print(user)
    rating = shop_ratings.get(user=user).rating
    # print(rating)
    return rating
