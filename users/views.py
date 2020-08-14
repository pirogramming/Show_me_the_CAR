from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from .forms import RatingForm
from . import models as user_models
from shops import models as shop_models


def render_mypage(request):
    user = request.user
    like_shops = user.like_shops.all()
    # rating = user.ratings.all().filter(shop=like_shops)
    # print(like_shops)
    rating_form = RatingForm()
    # print(rating_form)
    ctx = {
        "user": user,
        "like_shops": like_shops,
        "rating_form": rating_form,
    }

    return render(request, "users/mypage.html", ctx)


@require_POST
def rate_shop_ajax(request):
    user = request.user
    shop = shop_models.Shop.objects.get(id=request.POST.get("shop_id"))
    print(user)
    print(shop)
    my_rating = request.POST.get("my_rating")
    rating = shop_models.Rating.objects.get(user=user, shop=shop)
    rating.rating = my_rating
    rating.save()
    print(rating)
    data = {}
    return JsonResponse(data)

