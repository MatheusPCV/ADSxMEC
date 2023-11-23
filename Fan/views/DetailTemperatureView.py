from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from models.TemperatureModel import TemparatureEntity
from serializer.TemperatureSerializer import TemperatureEntitySerializer


class DetailFanEntityView(viewsets.ViewSet):

    serializer_class = TemperatureEntitySerializer

    def retrieve(self, request, pk=None):
            try:
                temperature_model = TemparatureEntity.objects.get(pk=pk)
                serializer = self.serializer_class(temperature_model)
                return Response(serializer.data)
            except TemparatureEntity.DoesNotExist:
                return Response(
                    {"error": "FanEntity not found"},
                    status=status.HTTP_404_NOT_FOUND
                )