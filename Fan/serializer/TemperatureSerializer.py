from rest_framework import serializers
from models.TemperatureModel import TemparatureEntity

class TemperatureEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemparatureEntity
        fields = '__all__'