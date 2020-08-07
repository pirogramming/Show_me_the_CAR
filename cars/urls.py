from django.contrib import admin
from django.urls import path

from .views import *


app_name = 'cars'

urlpatterns = [

    path('', admin.site.urls),
    path('search/', search_car, name='search_car')

]
