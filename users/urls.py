from django.urls import path
from . import views as user_views


app_name = "users"

urlpatterns = [
    path("mypage/", user_views.render_mypage, name="mypage"),
    path("rating/", user_views.rate_shop_ajax, name="rate_shop_ajax"),
]
