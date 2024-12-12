from .serializers import CarsSerializer, SensorsSerializer, ServiceCentersSerializer, MaintenanceSerializer
from .models import Cars, Sensors, ServiceCenters, Maintenance
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CarsViewSet(ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class CarsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class SensorsViewSet(ListCreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class SensorsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class MaintenanceViewSet(ListCreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class MaintenanceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer


class ServiceCentersViewSet(ListCreateAPIView):
    queryset = ServiceCenters.objects.all()
    serializer_class = ServiceCentersSerializer


class ServiceCentersDetail(RetrieveUpdateDestroyAPIView):
    queryset = ServiceCenters.objects.all()
    serializer_class = ServiceCentersSerializer
