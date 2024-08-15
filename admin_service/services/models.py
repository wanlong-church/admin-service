from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class ServiceNote(models.Model):
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('service:note-list')

    def __str__(self):
        return f"Note {self.id}"

class ServiceGroup(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('service:group-list')

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    service_group = models.ForeignKey(ServiceGroup, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.ManyToManyField(ServiceNote, blank=True)

    def get_absolute_url(self):
        return reverse('service:type-list')

    def __str__(self):
        return self.name

class Service(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('service:list')

    def __str__(self):
        return f"Service {self.id} - {self.service_type.name}"