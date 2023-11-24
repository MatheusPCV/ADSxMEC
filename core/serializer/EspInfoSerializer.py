from rest_framework import serializers
from core.models.EspInfoEntity import EspInfo

class EspInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspInfo
        fields = '__all__'