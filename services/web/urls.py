"""
URL configuration for service app web views.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.urls import path

from . import views

app_name = "service"

urlpatterns = [
    # Service Notes
    path("service-notes/", views.ServiceNoteListView.as_view(), name="note-list"),
    path(
        "service-notes/create/",
        views.ServiceNoteCreateView.as_view(),
        name="note-create",
    ),
    path(
        "service-notes/<int:pk>/update/",
        views.ServiceNoteUpdateView.as_view(),
        name="note-update",
    ),
    path(
        "service-notes/<int:pk>/delete/",
        views.ServiceNoteDeleteView.as_view(),
        name="note-delete",
    ),
    # Service Groups
    path("service-groups/", views.ServiceGroupListView.as_view(), name="group-list"),
    path(
        "service-groups/create/",
        views.ServiceGroupCreateView.as_view(),
        name="group-create",
    ),
    path(
        "service-groups/<int:pk>/update/",
        views.ServiceGroupUpdateView.as_view(),
        name="group-update",
    ),
    path(
        "service-groups/<int:pk>/delete/",
        views.ServiceGroupDeleteView.as_view(),
        name="group-delete",
    ),
    # Service Types
    path("service-types/", views.ServiceTypeListView.as_view(), name="type-list"),
    path(
        "service-types/create/",
        views.ServiceTypeCreateView.as_view(),
        name="type-create",
    ),
    path(
        "service-types/<int:pk>/update/",
        views.ServiceTypeUpdateView.as_view(),
        name="type-update",
    ),
    path(
        "service-types/<int:pk>/delete/",
        views.ServiceTypeDeleteView.as_view(),
        name="type-delete",
    ),
    # Services
    path("services/", views.ServiceListView.as_view(), name="list"),
    path("services/<int:pk>/", views.ServiceDetailView.as_view(), name="detail"),
    path("services/create/", views.ServiceCreateView.as_view(), name="create"),
    path("services/<int:pk>/update/", views.ServiceUpdateView.as_view(), name="update"),
    path("services/<int:pk>/delete/", views.ServiceDeleteView.as_view(), name="delete"),
]
