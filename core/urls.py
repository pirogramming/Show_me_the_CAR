from django.urls import path
from shops import views as shop_views
from . import views as core_views

app_name = "core"

urlpatterns = [
    path("", shop_views.home, name="home"),
    path("about_us/", core_views.about_us, name="about_us"),
]
