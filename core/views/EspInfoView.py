from core.serializer.EspInfoSerializer import EspInfoSerializer
from core.models.EspInfoEntity import EspInfo
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
import datetime




class EspInfoView(ViewSet):

    signal_status = True

    def list(self, request):
        esp_infos = EspInfo.objects.all()
        serializer = EspInfoSerializer(esp_infos, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        global signal_status
        
        # Verifica o estado do sinal antes de prosseguir
        if signal_status:
            serializer = EspInfoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Signal not active.'}, status=status.HTTP_403_FORBIDDEN)


