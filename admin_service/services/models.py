from django.db import models

# Create your models here.
from django.db import models

class ServiceNote(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"Note {self.id}"

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.ManyToManyField(ServiceNote, blank=True)

    def __str__(self):
        return self.name

class ServiceGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    service_group = models.ForeignKey(ServiceGroup, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"Service {self.id} - {self.service_type.name}"