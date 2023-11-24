from django.urls import path
from core_app.views import EspInfoView

urlpatterns = [
    path('', EspInfoView.as_view({'post': 'create', 'get': 'list'}), name='espinfo-list'),
]