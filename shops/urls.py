from django.urls import path

from . import views as shop_views


app_name = "shops"

urlpatterns = [
    path("", shop_views.ShopListView.as_view(), name="shop_list"),
    path("<int:id>/", shop_views.shop_detail, name="shop_detail"),
    path("search_main/", shop_views.ShopSearchView.as_view(), name="shop_search_main"),
    path("search_landing/", shop_views.ShopSearchView.as_view(), name="shop_search_landing"),
    path("like/", shop_views.shop_like_ajax, name="shop_like_ajax"),
]
