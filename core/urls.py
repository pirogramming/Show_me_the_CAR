from django.urls import path
from shops import views as shop_views

app_name = "core"

urlpatterns = [
    path("", shop_views.home, name="home"),
]
