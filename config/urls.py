from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("core.urls", namespace="core")), 
    path("rooms/", include("rooms.urls", namespace="rooms")),   # rooms/urls.py
    path("admin/", admin.site.urls), 
    ] # 02

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)