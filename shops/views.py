from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shops.models import *


def index(request):
    shops = Shop.objects.all()
    return render(request, 'shops/index.html', {'shops': shops})


def give_rating(request, pk):
    if request.method == 'POST':
        rating = get_object_or_404(Rating, pk=pk)
        rating.Rating = request.POST['rating']
        rating.save()
        return redirect(reverse('shops:give_rating', kwargs={'pk': pk}))

    shop = get_object_or_404(Shop, pk=pk)
    ratings = Rating.objects.values('rating')
    rating_sum = 0
    for r in ratings:
        r_value = list(r.values())
        rating_sum = rating_sum + sum(r_value)
    average = rating_sum/len(ratings)

    return render(request, 'shops/give_rating.html', {
        'shop': shop, 'average': average
    })
