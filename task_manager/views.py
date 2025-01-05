from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('index')
    success_message = 'You were logged in'
    extra_context = {
        'title': 'Log In',
        'button_name': 'Enter',
    }
