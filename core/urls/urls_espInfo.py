from django.contrib import admin
from django.urls import path, include
from app.views import EspInfoView, EspResetView



urlpatterns = [
    path("esp-reset/", EspResetView.as_view(), name="esp_reset"),
    path("esp-info/", EspInfoView.as_view(), name="esp_info"),
]
