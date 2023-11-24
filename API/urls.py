from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from core.urls import urls_espInfo,urls_espReset





urlpatterns = [
    path("espreset/", include(urls_espReset)),
    path("espinfo/", include(urls_espInfo)),
]
