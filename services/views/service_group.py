from ..models import ServiceGroup
from ..views.generics import (
    GenericCreateView,
    GenericDeleteView,
    GenericListView,
    GenericUpdateView,
)

__all__ = [
    "ServiceGroupListView",
    "ServiceGroupCreateView",
    "ServiceGroupUpdateView",
    "ServiceGroupDeleteView",
]


class ServiceGroupListView(GenericListView):
    model = ServiceGroup
    model_name = "Service Group"
    display_fields = ["name"]
    create_url = "service:group-create"
    update_url = "service:group-update"
    delete_url = "service:group-delete"


class ServiceGroupCreateView(GenericCreateView):
    model = ServiceGroup
    model_name = "Service Group"
    fields = ["name"]


class ServiceGroupUpdateView(GenericUpdateView):
    model = ServiceGroup
    model_name = "Service Group"
    fields = ["name"]


class ServiceGroupDeleteView(GenericDeleteView):
    model = ServiceGroup
    model_name = "Service Group"
    success_url_name = "service:group-list"
