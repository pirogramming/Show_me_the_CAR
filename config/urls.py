from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # shops
    path("shops/", include("shops.urls", namespace="shops")),
    # login
    path("login/", include("login.urls", namespace="login")),
    path("accounts/", include("allauth.urls"),),
    path("users/", include("users.urls", namespace="users")),
    # search
    path("cars/", include("cars.urls", namespace="cars")),
    path("", include("core.urls", namespace="core")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
