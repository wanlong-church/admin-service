from typing import List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

__all__ = ["BaseObjectView"]


class BaseObjectView(LoginRequiredMixin, View):
    """
    A mixin that provides common context data for views.
    """

    model_name: str = ""
    model_name_plural: str = ""
    display_fields: List[str] = []

    def get_context_data(self, **kwargs):
        """
        Add common context data to the view.

        :param kwargs: Additional keyword arguments
        :return: Updated context dictionary
        :rtype: dict
        """
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model_name
        context["model_name_plural"] = self.model_name_plural or f"{self.model_name}s"
        return context
