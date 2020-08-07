from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse

from cars.models import *
from shops.models import *


def search_car(request):
    if request.method == "POST":
        query = request.GET.get("q")
        qs = Car.objects.all()
        if query:
            qs = qs.filter(Q(model_name__icontains=query)).values("shop")
            return redirect(reverse("shops:shop_list"), kwargs={"shops": qs})
    return render(request, "cars/search.html")

