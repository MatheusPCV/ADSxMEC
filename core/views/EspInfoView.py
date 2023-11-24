from core.serializer.EspInfoSerializer import EspInfoSerializer
from core.models.EspInfoEntity import EspInfo
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime




class EspInfoView(APIView):
    def post(self, request, format=None):
        serializer = EspInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


