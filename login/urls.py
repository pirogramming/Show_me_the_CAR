from django.urls import path
from login import views as login_views

app_name = "login"

urlpatterns = [
    path("", login_views.home, name="login"),
]
