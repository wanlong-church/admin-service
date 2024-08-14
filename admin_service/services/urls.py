"""
URL configuration for service app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('service-types/', views.ServiceTypeList.as_view(), name='type-list'),
    path('service-types/<int:pk>/', views.ServiceTypeDetail.as_view(), name='type-detail'),
    path('service-groups/', views.ServiceGroupList.as_view(), name='group-list'),
    path('service-groups/<int:pk>/', views.ServiceGroupDetail.as_view()),
    path('service-notes/', views.ServiceNoteList.as_view(), name='note-list'),
    path('service-notes/<int:pk>/', views.ServiceNoteDetail.as_view(), name='note-detail'),
    path('services/', views.ServiceList.as_view(), name='list'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='detail'),
]
