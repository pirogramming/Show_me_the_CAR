from .models import Login
from django.contrib import admin
from . import models

@admin.register(models.Login)
class LoginAdmin(admin.ModelAdmin):

    """ Login Admin Definition """
    pass
