from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from core.serializer import EspInfoSerializer
from core.models import EspInfoEntity
from django.utils import timezone

class EspInfoViewSet(ModelViewSet):
    queryset = EspInfoEntity.objects.all()
    serializer_class = EspInfoSerializer

    def create(self, request, *args, **kwargs):
        today = timezone.now().date()
        existing_info = EspInfoEntity.objects.filter(data=today).first()
        if existing_info:
            serializer = self.serializer_class(existing_info, data=request.data)
        else:
            serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        today = timezone.now().date()
        esp_infos = EspInfoEntity.objects.filter(data=today)
        serializer = self.serializer_class(esp_infos, many=True)
        return Response(serializer.data)
