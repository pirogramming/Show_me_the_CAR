"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = bool(os.environ.get("DEBUG"))
DEBUG = True

ALLOWED_HOSTS = [".elasticbeanstalk.com"]
print(f"DEBUG: {DEBUG}")


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    # "django.contrib.sites",  # login
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",  # widgets
    # "allauth",
    # "allauth.account",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.google",
    # "allauth.socialaccount.providers.naver",
    # "allauth.socialaccount.providers.kakao",
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "shops.apps.ShopsConfig",
    "cars.apps.CarsConfig",
    "login.apps.LoginConfig",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


if DEBUG is False:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

else:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("RDS_HOST"),
            "NAME": os.environ.get("RDS_NAME"),
            "USER": os.environ.get("RDS_USER"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "PORT": "5432",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

AUTH_USER_MODEL = "users.User"

# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# )

SITE_ID = 1
# LOGIN_REDIRECT_URL = "/"

# users/models.py avatar
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

FORM_RENDERER = (
    "django.forms.renderers.TemplatesSetting"  # 위젯 폼 렌더링 문제, 왜 발생하는지 모르겠는데 이거 넣으면 해결됨
)

