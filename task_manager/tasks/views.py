from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from task_manager.mixins import CustomLoginRequiredMixin
from task_manager.tasks.forms import TaskCreationForm
from task_manager.tasks.models import Task


class TaskListView(CustomLoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"
    ordering = ["id"]
    extra_context = {"title": _("Tasks"), "create": _("Create task")}


class TaskInfoView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_info.html"
    context_object_name = "task"
    extra_context = {
        "title": _("Task"),
        "author": _("Author"),
        "performer": _("Performer"),
        "status": _("Status"),
        "createdate": _("Creation Date"),
        "update": _("Last update"),
    }


class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    template_name = "form.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task was created successfully")
    extra_context = {"title": _("Create task"), "button_name": _("Create")}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    template_name = "form.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task was updated successfully")
    extra_context = {"title": _("Update task"), "button_name": _("Update")}


class TaskDeleteView(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task was deleted successfully")
    permission_denied_url = reverse_lazy("tasks_list")
    permission_denied_message = _("Only the task's author can delete it")
    extra_context = {"title": _("Delete task"), "button_name": _("Yes, delete")}
