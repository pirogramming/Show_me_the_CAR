from django.contrib.auth.models import AbstractUser
from django.db import models
from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model """

    avatar = models.ImageField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    superhost = models.BooleanField(default=False)
    objects = core_managers.CustomUserManager()
