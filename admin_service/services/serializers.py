from rest_framework import serializers
from .models import ServiceType, ServiceGroup, ServiceNote, Service

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class ServiceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGroup
        fields = '__all__'

class ServiceNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceNote
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'