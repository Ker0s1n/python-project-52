from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelCreationForm
from task_manager.labels.models import Label
from task_manager.mixins import CustomLoginRequiredMixin, ProtectErrorMixin


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels_list.html"
    context_object_name = "labels"
    ordering = ["id"]
    extra_context = {
        "title": _("Labels"),
        "create": _("Create label"),
        "edit": _("Edit"),
        "delete": _("Delete"),
    }


class LabelCreateView(
    CustomLoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = Label
    template_name = "form.html"
    form_class = LabelCreationForm
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was created successfully")
    extra_context = {"title": _("Create label"), "button_name": _("Create")}


class LabelUpdateView(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    form_class = LabelCreationForm
    model = Label
    template_name = "form.html"
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was updated successfully")
    extra_context = {
        "title": _("Update label"),
        "button_name": _("Update"),
    }


class LabelDeleteView(
    CustomLoginRequiredMixin,
    ProtectErrorMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = "labels/label_delete.html"
    model = Label
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was deleted successfully")
    protected_object_url = reverse_lazy("labels_list")
    protected_object_message = _(
        "Cannot delete this label because it is being used"
    )
    extra_context = {
        "title": _("Delete label"),
        "button_name": _("Yes, delete"),
    }
