from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..models import Service, ServiceGroup, ServiceNote, ServiceType

# Service Note Views


class ServiceNoteListView(ListView):
    model = ServiceNote
    template_name = "services/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = ["content"]
        context["model_name"] = "Service Note"
        context["model_name_plural"] = "Service Notes"
        context["create_url"] = "service:note-create"
        context["update_url"] = "service:note-update"
        context["delete_url"] = "service:note-delete"
        return context


class ServiceNoteCreateView(CreateView):
    model = ServiceNote
    fields = ["content"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Note"
        return context


class ServiceNoteUpdateView(UpdateView):
    model = ServiceNote
    fields = ["content"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Note"
        return context


class ServiceNoteDeleteView(DeleteView):
    model = ServiceNote
    success_url = reverse_lazy("service:note-list")
    template_name = "services/generic_confirm_delete.html"


# Service Group Views


class ServiceGroupListView(ListView):
    model = ServiceGroup
    template_name = "services/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = ["name"]
        context["model_name"] = "Service Group"
        context["model_name_plural"] = "Service Groups"
        context["create_url"] = "service:group-create"
        context["update_url"] = "service:group-update"
        context["delete_url"] = "service:group-delete"
        return context


class ServiceGroupCreateView(CreateView):
    model = ServiceGroup
    fields = ["name"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Group"
        return context


class ServiceGroupUpdateView(UpdateView):
    model = ServiceGroup
    fields = ["name"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Group"
        return context


class ServiceGroupDeleteView(DeleteView):
    model = ServiceGroup
    success_url = reverse_lazy("service:group-list")
    template_name = "services/generic_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Group"
        return context


# Service Type Views


class ServiceTypeListView(ListView):
    model = ServiceType
    template_name = "services/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = [
            "name",
            "start_time",
            "end_time",
            "service_group",
            "notes",
        ]
        context["model_name"] = "Service Type"
        context["model_name_plural"] = "Service Types"
        context["create_url"] = "service:type-create"
        context["update_url"] = "service:type-update"
        context["delete_url"] = "service:type-delete"
        return context


class ServiceTypeCreateView(CreateView):
    model = ServiceType
    fields = ["name", "service_group", "start_time", "end_time", "notes"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Type"
        return context


class ServiceTypeUpdateView(UpdateView):
    model = ServiceType
    fields = ["name", "service_group", "start_time", "end_time", "notes"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Type"
        return context


class ServiceTypeDeleteView(DeleteView):
    model = ServiceType
    success_url = reverse_lazy("service:type-list")
    template_name = "services/generic_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service Type"
        return context


# Service Views


class ServiceListView(ListView):
    model = Service
    template_name = "services/generic_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_fields"] = ["service_type", "date"]
        context["model_name"] = "Service"
        context["model_name_plural"] = "Services"
        context["create_url"] = "service:create"
        context["update_url"] = "service:update"
        context["delete_url"] = "service:delete"
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/generic_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service"
        return context


class ServiceCreateView(CreateView):
    model = Service
    fields = ["service_type", "date"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service"
        return context


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ["service_type", "date"]
    template_name = "services/generic_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service"
        return context


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy("service:list")
    template_name = "services/generic_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = "Service"
        return context
