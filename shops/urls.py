from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    path('list/', views.shop_list, name='shop_list'),
    path('<int:shop_id>/like/', views.like, name='like'),
]