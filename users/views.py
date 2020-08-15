from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_POST

from .forms import RatingForm
from .models import User
from shops.models import Rating, Shop
from shops.forms import SearchForm


def render_mypage(request):
    user = request.user
    like_shops = user.like_shops.all()
    car_model = request.GET.get("car_model")
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


# @require_POST
def rate_shop_ajax(request):
    print(request.POST)
    rating_value = request.POST["rating"]
    print(rating_value)
    shop_id = request.POST["shop_id"]
    print(shop_id)
    rating = Rating.objects.get(user_id=request.user.id, shop_id=shop_id)
    rating.rating = rating_value
    rating.save()
    url = reverse("users:mypage")
    return redirect(to=url)
    # data = {}
    # return JsonResponse(data)

