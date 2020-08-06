from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Shop
from users.models import User


def shop_list(request):
    shops = Shop.objects.all()
    ctx = {
        'shops': shops
    }
    return render(request, 'shops/shop_list.html', ctx)


def like(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    user = request.user
    # 좋아요 기능, user가heart를 눌렀을 때, 대리점의 like_users list에 있으면 list에서 삭제되고 없으면 추가된다
    if user in shop.like_users.all():
        shop.like_users.remove(user)
    else:
        shop.like_users.add(user)
    return redirect('shops:shop_list')
