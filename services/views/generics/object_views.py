from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from services.views.generics import BaseObjectView


class GenericListView(BaseObjectView, ListView):
    """
    A generic list view that includes common context data.
    """

    template_name = "services/generic_list.html"
    create_url: str
    update_url: str
    delete_url: str

    def get_context_data(self, **kwargs):
        """
        Add list-specific context data to the view.

        :param kwargs: Additional keyword arguments
        :return: Updated context dictionary
        :rtype: dict
        """
        context = super().get_context_data(**kwargs)
        context["display_fields"] = self.display_fields
        context["create_url"] = self.create_url
        context["update_url"] = self.update_url
        context["delete_url"] = self.delete_url
        return context


class GenericCreateView(BaseObjectView, CreateView):
    """
    A generic create view that includes common context data.
    """

    template_name = "services/generic_form.html"


class GenericUpdateView(BaseObjectView, UpdateView):
    """
    A generic update view that includes common context data.
    """

    template_name = "services/generic_form.html"


class GenericDeleteView(BaseObjectView, DeleteView):  # type: ignore
    """
    A generic delete view that includes common context data.
    ignoring mypy errors, see: https://github.com/typeddjango/django-stubs/issues/1227
    """

    template_name = "services/generic_confirm_delete.html"
    success_url_name: str

    def get_success_url(self):
        """
        Get the URL to redirect to after successful deletion.

        :return: Success URL
        :rtype: str
        """
        return reverse_lazy(self.success_url_name)
