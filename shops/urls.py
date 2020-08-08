from django.contrib import admin
from django.urls import path

from . import views as shop_views


app_name = "shops"

urlpatterns = [
    path("give_rating/<int:id>/", shop_views.give_rating, name="give_rating"),
    # path("list/", shop_views.SearchView.as_view(), name="shop_list"),
    path("<int:shop_id>/like/", shop_views.like, name="like"),
    path("search/", shop_views.search, name="search"),
]
