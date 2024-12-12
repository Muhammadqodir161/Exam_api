from rest_framework import serializers
from .models import Cars, Sensors, ServiceCenters, Maintenance

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'model', 'year', 'vin']

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'type', 'installed_date', 'cars']

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'service_type', 'service_date', 'cars']

class ServiceCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenters
        fields = ['id', 'name', 'address', 'rating']