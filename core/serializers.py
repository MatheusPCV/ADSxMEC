from rest_framework import serializers
from .models import EspInfo
from .models import EspReset

class EspInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspInfo
        fields = '__all__'

class EspResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspReset
        fields = '__all__'