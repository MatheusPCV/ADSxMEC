
from django.urls import path, include
from core.views.EspInfoView import EspInfoViewSet # Certifique-se de importar a classe EspInfoViewSet corretamente

urlpatterns = [
    path('espinfo/', EspInfoViewSet.as_view({'get': 'list', 'post': 'create'}), name='espinfo'),  
]