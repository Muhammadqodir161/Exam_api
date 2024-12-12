from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=100)
    year = models.DateField()
    vin = models.CharField(max_length=17)

    def __str__(self):
        return self.model

class Sensors(models.Model):
    type = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Cars, on_delete=models.CASCADE)
    installed_date = models.DateField()

    def __str__(self):
        return self.type

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Cars, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    service_date = models.DateField()

    def __str__(self):
        return self.service_type

class ServiceCenters(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name
