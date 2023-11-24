
from django.urls import path, include
from core.views.EspInfoView import EspInfoView



urlpatterns = [
    path("", EspInfoView.as_view({'post': 'create','get':'list'}), name="esp_reset"),
    
]
