from django.urls import path

from . import views as shop_views


app_name = "shops"

urlpatterns = [
    path("", shop_views.ShopListView.as_view(), name="shop_list"),
    path("<int:id>/", shop_views.shop_detail, name="shop_detail"),
    path("search/", shop_views.ShopSearchView.as_view(), name="shop_search"),
    path("<int:shop_id>/like/", shop_views.shop_like, name="shop_like"),
]