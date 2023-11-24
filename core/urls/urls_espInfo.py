
from django.urls import path, include
from app.views import EspResetView



urlpatterns = [
    path("", EspResetView.as_view({'post': 'create'}), name="esp_reset"),
    
]
