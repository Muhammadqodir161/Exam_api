from django.urls import path
from .views import CarsDetail, CarsViewSet, SensorsDetail, SensorsViewSet, ServiceCentersDetail, \
    ServiceCentersViewSet, MaintenanceDetail, MaintenanceViewSet

urlpatterns = [
    path('cars/', CarsViewSet.as_view()),
    path('cars/<int:pk>/', CarsDetail.as_view()),
    path('sensors/', SensorsViewSet.as_view()),
    path('sensors/<int:pk>/', SensorsDetail.as_view()),
    path('maintenance/', MaintenanceViewSet.as_view()),
    path('maintenance/<int:pk>/', MaintenanceDetail.as_view()),
    path('servicecenters/', ServiceCentersViewSet.as_view()),
    path('servicecenters/<int:pk>/', ServiceCentersDetail.as_view()),

]