from django.urls import path
from . import views as login_views

app_name = "login"

urlpatterns = [
    path("", login_views.login_page, name="login_page"),
    path("kakao/", login_views.kakao_login, name="kakao-login"),
    path("kakao/callback/", login_views.kakao_callback, name="kakao-callback"),
    path("naver/", login_views.naver_login, name="naver-login"),
    path("naver/callback/", login_views.naver_callback, name="naver-callback"),
    path("google/", login_views.google_login, name="google-login"),
    path("google/callback/", login_views.google_callback, name="google-callback"),
    path("logout_page/", login_views.logout_page, name="logout_page"),
    path("logout/", login_views.log_out, name="logout"),
]
