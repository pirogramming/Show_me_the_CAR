from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shops.models import *


def index(request):
    shops = Shop.objects.all()
    return render(request, 'shops/index.html', {'shops': shops})


def give_rating(request, pk):
    # POST 방식
    # 나의 평점을 POST 방식으로 추가하면 rating query에 평점이 등록됨
    if request.method == 'POST':
        rating = get_object_or_404(Rating, pk=pk)
        rating.Rating = request.POST['rating']
        rating.save()
        return redirect(reverse('shops:give_rating', kwargs={'pk': pk}))

    # GET 방식
    shop = get_object_or_404(Shop, pk=pk)

    # 특정 샵의 Pk로 먼저 필터링 후 그 샵의 rating field 값만 불러와서 리스트 생성
    ratings = Rating.objects.filter(shop=pk).values('rating')

    # 생성한 ratings 딕셔너리에서 value 값만 추출해서 평균 구하는 루프
    rating_sum = 0
    for r in ratings:
        r_value = list(r.values())
        rating_sum = rating_sum + sum(r_value)
    average = rating_sum/len(ratings)

    return render(request, 'shops/give_rating.html', {
        'shop': shop, 'average': average
    })

