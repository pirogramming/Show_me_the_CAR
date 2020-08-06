from django.shortcuts import render
from shops.models import *


def index(request):
    shops = Shop.objects.all()
    return render(request, 'shops/index.html', {'shops': shops})

