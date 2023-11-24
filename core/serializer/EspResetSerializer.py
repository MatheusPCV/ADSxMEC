from rest_framework import serializers
from core.models.EspResetEntity import EspReset


class EspResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspReset
        fields = '__all__'