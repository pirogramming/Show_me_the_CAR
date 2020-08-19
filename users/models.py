from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    LOGIN_NAVER = "naver"
    LOGIN_GOOGLE = "google"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_NAVER, "Naver"),
        (LOGIN_GOOGLE, "Google"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_KAKAO
    )
