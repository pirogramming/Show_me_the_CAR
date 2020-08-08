from django.shortcuts import render
from cars import models as cars_models
from shops import models as shops_models


def car_list(request):
    cars = cars_models.Car.objects.all()[0:10]
    context = {
        "cars": cars,
    }
    return render(request, "cars/car_list.html", context=context)


def car_detail(request, pk):
    car = cars_models.Car.objects.get(pk=pk)
    # shops = shops_models.Shop.objects.get(id=1)
    # print(dir(shops))
    context = {
        "car": car,
    }
    return render(request, "cars/car_detail.html", context=context)
