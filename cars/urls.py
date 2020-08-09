from django.urls import path

from . import views as car_views


app_name = "cars"

urlpatterns = [
    path("", car_views.car_list, name="car_list"),
    path("<int:pk>/detail/", car_views.car_detail, name="car_detail"),
    path("main_search/", car_views.main_search, name='main_search'),
]
