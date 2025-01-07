from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")
    redirect_field_name = None
    access_denied_message = "You are not authorized! Please, log in."

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.ERROR, self.access_denied_message
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    permission_denied_url = None
    permission_denied_message = "Permission denied"

    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.add_message(
                request, messages.ERROR, self.permission_denied_message
            )
            return redirect(self.permission_denied_url)
        return super().dispatch(request, *args, **kwargs)
