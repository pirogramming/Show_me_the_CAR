import os
import requests
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from users import models as user_models


def login_page(request):
    return render(request, "login/login.html")


def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    print(client_id)
    redirect_uri = "http://127.0.0.1:8000/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    )


class KakaoException(Exception):
    print("Kakao error!")


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        redirect_uri = "http://127.0.0.1:8000/login/kakao/callback"
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        # print(token_json)
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        print(profile_json)
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email")
        print(email)
        if email is None:
            raise KakaoException()
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        thumbnail_image = properties.get("profile_image")
        try:
            user = user_models.User.objects.get(email=email)
            if user.login_method != user_models.User.LOGIN_KAKAO:
                raise KakaoException()
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=user_models.User.LOGIN_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
        print(user)
        login(request, user)
        return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("login:login_page"))
