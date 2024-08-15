from ..models import ServiceType
from ..views.generics import (
    GenericCreateView,
    GenericDeleteView,
    GenericListView,
    GenericUpdateView,
)

__all__ = [
    "ServiceTypeListView",
    "ServiceTypeCreateView",
    "ServiceTypeUpdateView",
    "ServiceTypeDeleteView",
]


class ServiceTypeListView(GenericListView):
    model = ServiceType
    model_name = "Service Type"
    display_fields = ["name", "start_time", "end_time", "service_group", "notes"]
    create_url = "service:type-create"
    update_url = "service:type-update"
    delete_url = "service:type-delete"


class ServiceTypeCreateView(GenericCreateView):
    model = ServiceType
    model_name = "Service Type"
    fields = ["name", "service_group", "start_time", "end_time", "notes"]


class ServiceTypeUpdateView(GenericUpdateView):
    model = ServiceType
    model_name = "Service Type"
    fields = ["name", "service_group", "start_time", "end_time", "notes"]


class ServiceTypeDeleteView(GenericDeleteView):
    model = ServiceType
    model_name = "Service Type"
    success_url_name = "service:type-list"
