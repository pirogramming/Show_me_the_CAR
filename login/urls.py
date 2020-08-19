from django.urls import path
from . import views as login_views

app_name = "login"

urlpatterns = [
    path("", login_views.login_page, name="login_page"),
    path("kakao/", login_views.kakao_login, name="kakao-login"),
    path("kakao/callback", login_views.kakao_callback, name="kakao-callback"),
]
