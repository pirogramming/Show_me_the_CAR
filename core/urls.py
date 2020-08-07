from django.urls import path
from cars import views as car_views

app_name = "cars"

urlpatterns = [
    path("", car_views.search_car, name="search_car"),
]
