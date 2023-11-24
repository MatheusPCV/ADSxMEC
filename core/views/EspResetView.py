from core.serializer.EspResetSerializer import EspResetSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
import datetime
from core.models.EspResetEntity import EspReset


class EspResetView(ViewSet):

    signal_status = False

    def create(self, request, *args, **kwargs):
        global signal_status
        
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

        # Atualiza o estado do sinal
        signal_status = esp_reset.signal_to_send

        serializer = EspResetSerializer(esp_reset)
        return Response(serializer.data, status=status.HTTP_200_OK)