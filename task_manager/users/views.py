from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class UserListView(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"
    context_object_name = "users"
    ordering = ["id"]


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = "form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("users_list")
    success_message = "User was registered successfully"
    extra_context = {"title": "Sign Up", "button_name": "Register"}


class UserDeleteView(DeleteView):
    template_name = "users/user_delete.html"
    model = get_user_model()
    success_url = reverse_lazy("users_list")
    success_message = "User was deleted successfully"
    extra_context = {"button_name": "Yes, delete"}


class UserUpdateView(UpdateView):
    form_class = UserCreationForm
    model = get_user_model()
    template_name = "form.html"
    success_url = reverse_lazy("user_list")
    success_message = "User was updated successfully"
    extra_context = {
        "button_name": "Update",
        "title": "Update User",
    }
