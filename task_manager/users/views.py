from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.forms import (
    CustomUserCreationForm,
    CustomUserUpdateForm,
)


class UserListView(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"
    context_object_name = "users"
    ordering = ["id"]


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    template_name = "form.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = "User was registered successfully"
    extra_context = {"title": "Sign Up", "button_name": "Register"}


class UserDeleteView(SuccessMessageMixin, DeleteView):
    template_name = "users/user_delete.html"
    model = get_user_model()
    success_url = reverse_lazy("users_list")
    success_message = "User was deleted successfully"
    extra_context = {"button_name": "Yes, delete"}


class UserUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CustomUserUpdateForm
    model = get_user_model()
    template_name = "form.html"
    success_url = reverse_lazy("users_list")
    success_message = "User was updated successfully"
    extra_context = {
        "button_name": "Update",
        "title": "Update User",
    }
