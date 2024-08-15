from ..models import ServiceNote
from ..views.generics import (
    GenericCreateView,
    GenericDeleteView,
    GenericListView,
    GenericUpdateView,
)

__all__ = [
    "ServiceNoteListView",
    "ServiceNoteCreateView",
    "ServiceNoteUpdateView",
    "ServiceNoteDeleteView",
]


class ServiceNoteListView(GenericListView):
    model = ServiceNote
    model_name = "Service Note"
    display_fields = ["content"]
    create_url = "service:note-create"
    update_url = "service:note-update"
    delete_url = "service:note-delete"


class ServiceNoteCreateView(GenericCreateView):
    model = ServiceNote
    model_name = "Service Note"
    fields = ["content"]


class ServiceNoteUpdateView(GenericUpdateView):
    model = ServiceNote
    model_name = "Service Note"
    fields = ["content"]


class ServiceNoteDeleteView(GenericDeleteView):
    model = ServiceNote
    model_name = "Service Note"
    success_url_name = "service:note-list"
