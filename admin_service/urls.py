"""
URL configuration for admin_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

handler404 = "admin_service.errors.handler404"

urlpatterns = [
    path("accounts/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("accounts/login/", LoginView.as_view(next_page="service:list"), name="login"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include("services.api.urls", namespace="api")),
    path("web/", include("services.urls", namespace="web")),
]
