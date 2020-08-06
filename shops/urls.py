from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'shops'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('detail/<int:pk>', detail, name='detail'),
    path('detail/<int:pk>/give_rating/', give_rating, name='give_rating'),
]
