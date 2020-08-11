from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import RatingForm
from .models import User
from shops.models import Rating, Shop


def render_mypage(request):
    user = request.user
    like_shops = user.like_shops.all()
    form = RatingForm()
    ctx = {
        'user': user,
        'like_shops': like_shops,
        'form': form
    }

    return render(request, 'users/mypage.html', ctx)


def rate_shop(request):

    for shop_id, star in request.POST.items():
        if star:
            rating = Rating.objects.get(user_id=request.user.id, shop_id=shop_id)
            rating.rating = star[0]
            rating.save()

    url = reverse('users:mypage')
    return redirect(to=url)