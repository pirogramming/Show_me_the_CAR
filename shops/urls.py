from django.contrib import admin
from django.urls import path

from . import views as shop_views


app_name = "shops"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("give_rating/<int:id>/", shop_views.give_rating, name="give_rating"),
    path("list/", shop_views.shop_list, name="shop_list"),
    path("<int:shop_id>/like/", shop_views.like, name="like"),
]
