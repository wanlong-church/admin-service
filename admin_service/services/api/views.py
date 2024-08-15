from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from ..models import ServiceType, ServiceGroup, ServiceNote, Service
from ..serializers import ServiceTypeSerializer, ServiceGroupSerializer, ServiceNoteSerializer, ServiceSerializer

class ServiceTypeList(generics.ListCreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

class ServiceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

class ServiceGroupList(generics.ListCreateAPIView):
    queryset = ServiceGroup.objects.all()
    serializer_class = ServiceGroupSerializer

class ServiceGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceGroup.objects.all()
    serializer_class = ServiceGroupSerializer

class ServiceNoteList(generics.ListCreateAPIView):
    queryset = ServiceNote.objects.all()
    serializer_class = ServiceNoteSerializer

class ServiceNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceNote.objects.all()
    serializer_class = ServiceNoteSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
