from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
    UserChangeForm,
    UserCreationForm,
)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name',) + UserCreationForm.Meta.fields


class CustomUserUpdateForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username')