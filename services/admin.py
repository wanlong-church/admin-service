from django.contrib import admin

from .models import Service, ServiceGroup, ServiceNote, ServiceType

admin.site.register(ServiceNote)
admin.site.register(ServiceType)
admin.site.register(ServiceGroup)
admin.site.register(Service)
