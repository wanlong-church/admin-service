from django.contrib import admin
from .models import ServiceNote, ServiceType, ServiceGroup, Service

admin.site.register(ServiceNote)
admin.site.register(ServiceType)
admin.site.register(ServiceGroup)
admin.site.register(Service)