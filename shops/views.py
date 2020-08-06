from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shops.models import *


def index(request):
    shops = Shop.objects.all()
    return render(request, 'shops/index.html', {'shops': shops})


def detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shops/detail.html', {'shop': shop})


def give_rating(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        shop.rating = request.POST['rating']
        shop.save()
        return redirect(reverse('shops:give_rating', kwargs={'pk': pk}))

    return render(request, 'shops/give_rating.html', {'shop': shop})
