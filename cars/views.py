from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from cars import models as cars_models
from shops import models as shops_models
from shops import urls


def car_list(request):
    cars = cars_models.Car.objects.all()[:10]
    context = {
        "cars": cars,
    }
    return render(request, "cars/car_list.html", context=context)


def car_detail(request, pk):
    try:
        car = cars_models.Car.objects.get(pk=pk)
        # shops = shops_models.Shop.objects.get(id=1)
        # print(dir(shops))
        context = {
            "car": car,
        }
        return render(request, "cars/car_detail.html", context=context)
    except cars_models.Car.DoesNotExist:
        raise Http404()


def main_search(request):
    query = request.GET.get('q', None)
    if query:
        return redirect(reverse('shops:shop_list') + '?q=' + query)
    return render(request, 'cars/search.html')