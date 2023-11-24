from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from core.views.EspInfoView import EspInfoView
from core.views.EspResetView import EspResetView


schema_view = get_schema_view(
    openapi.Info(
        title="API OCR",
        default_version='v0.1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("espreset/", include(EspResetView)),
    path("espinfo/", include(EspInfoView)),
]
