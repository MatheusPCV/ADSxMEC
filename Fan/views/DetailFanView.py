from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from models.FanModel import FanEntity
from serializer.FanSerializer import FanEntitySerializer


class DetailFanEntityView(viewsets.ViewSet):

    serializer_class = FanEntitySerializer
    def retrieve(self, request, pk=None):
            try:
                fan_entity = FanEntity.objects.get(pk=pk)
                serializer = self.serializer_class(fan_entity)
                return Response(serializer.data)
            except FanEntity.DoesNotExist:
                return Response(
                    {"error": "FanEntity not found"},
                    status=status.HTTP_404_NOT_FOUND
                )