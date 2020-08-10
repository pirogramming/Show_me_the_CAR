from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import User
from shops.models import Rating



def render_mypage(request):
    user = request.user
    like_shops = user.like_shops.all()
    ctx = {
        'user': user,
        'like_shops': like_shops
    }

    return render(request, 'users/mypage.html', ctx)


def rate_shop(request):
    for shop_id, star in request.POST.items():
        if not star:
            pass
        rating = Rating.objects.get(user_id=request.user.id, shop_id=shop_id)
        rating.rating = star
        rating.save()
    url = reverse('users:mypage')
    return redirect(to=url)