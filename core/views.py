from .serializers import EspInfoSerializer
from .serializers import EspResetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime

from .models import EspInfo
from .models import EspReset


class EspInfoView(APIView):
    def post(self, request, format=None):
        serializer = EspInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EspResetView(APIView):
    def post(self, request, *args, **kwargs):
        esp_reset = EspReset()
        esp_reset.last_notified_at = datetime.datetime.now()

        # Verifica se a hora atual é 00:00:00
        current_time = esp_reset.last_notified_at.time()
        esp_reset.signal_to_send = (
            current_time.hour == 0
            and current_time.minute == 0
            and current_time.second == 0
        )

        esp_reset.save()

        serializer = EspResetSerializer(esp_reset)
        return Response(serializer.data, status=status.HTTP_200_OK)
