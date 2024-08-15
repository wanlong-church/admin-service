from ..models import Service
from ..views.generics import (
    GenericCreateView,
    GenericDeleteView,
    GenericListView,
    GenericUpdateView,
)

__all__ = [
    "ServiceListView",
    "ServiceCreateView",
    "ServiceUpdateView",
    "ServiceDeleteView",
]


class ServiceListView(GenericListView):
    model = Service
    model_name = "Service"
    display_fields = ["service_type", "date"]
    create_url = "service:create"
    update_url = "service:update"
    delete_url = "service:delete"


class ServiceCreateView(GenericCreateView):
    model = Service
    model_name = "Service"
    fields = ["service_type", "date"]


class ServiceUpdateView(GenericUpdateView):
    model = Service
    model_name = "Service"
    fields = ["service_type", "date"]


class ServiceDeleteView(GenericDeleteView):
    model = Service
    model_name = "Service"
    success_url_name = "service:list"
