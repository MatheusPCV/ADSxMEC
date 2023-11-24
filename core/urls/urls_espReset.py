from django.urls import path
from core.views.EspResetView import EspResetView

urlpatterns = [
    path('', EspResetView.as_view({'post': 'create'}), name='espinfo-list'),
]