from django.contrib import admin
from django.urls import path

from .views import *


app_name = 'shops'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('give_rating/<int:pk>', give_rating, name='give_rating'),
    path('list/', shop_list, name='shop_list'),
    path('<int:shop_id>/like/', like, name='like'),
]
