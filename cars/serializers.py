from rest_framework import serializers

from .models import CarRecord


class CarRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRecord
        fields = '__all__'
