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
    pass


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
        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email")
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
        login(request, user)
        return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("login:login_page"))


def naver_login(request):
    client_id = os.environ.get("NAVER_ID")
    request_uri = "http://127.0.0.1:8000/login/naver/callback"
    state = request.GET.get("csrfmiddlewaretoken")
    return redirect(
        f"https://nid.naver.com/oauth2.0/authorize?client_id={client_id}&response_type=code&redirect_uri={request_uri}&state={state}"
    )


class NaverException(Exception):
    pass


def naver_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("NAVER_ID")
        client_secret = os.environ.get("NAVER_SECRET")
        state = request.GET.get("state")
        token_request = requests.get(
            f"https://nid.naver.com/oauth2.0/token?client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&state={state}&code={code}"
        )
        token_json = token_request.json()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://openapi.naver.com/v1/nid/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        response = profile_json.get("response")
        email = response.get("email")
        if email is None:
            raise NaverException()
        nickname = response.get("name")
        thumbnail_image = response.get("profile_image")
        try:
            user = user_models.User.objects.get(email=email)
            if user.login_method != user_models.User.LOGIN_NAVER:
                raise NaverException()
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=user_models.User.LOGIN_NAVER,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        return redirect(reverse("core:home"))
    except NaverException:
        return redirect(reverse("login:login_page"))


def google_login(request):
    client_id = os.environ.get("GOOGLE_ID")
    request_uri = "http://127.0.0.1:8000/login/google/callback"
    scope = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
    include_granted_scopes = "true"
    access_type = "offline"
    state = request.GET.get("csrfmiddlewaretoken")
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={request_uri}&state={state}&scope={scope}&include_granted_scopes={include_granted_scopes}&access_type={access_type}"
    )


class GoogleException(Exception):
    pass


def google_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("GOOGLE_ID")
        client_secret = os.environ.get("GOOGLE_SECRET")
        request_uri = "http://127.0.0.1:8000/login/google/callback"
        token_request = requests.post(
            f"https://oauth2.googleapis.com/token?grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}&redirect_uri={request_uri}"
        )
        token_json = token_request.json()
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        response = profile_request.json()
        email = response.get("email")
        if email is None:
            raise GoogleException()
        nickname = response.get("name")
        thumbnail_image = response.get("picture")
        try:
            user = user_models.User.objects.get(email=email)
            if user.login_method != user_models.User.LOGIN_GOOGLE:
                raise GoogleException()
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=user_models.User.LOGIN_GOOGLE,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        return redirect(reverse("core:home"))
    except GoogleException:
        return redirect(reverse("login:login_page"))


def logout_page(request):
    return render(request, "login/logout.html")


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
