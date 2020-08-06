from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'shops'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('give_rating/<int:pk>', give_rating, name='give_rating'),
]
