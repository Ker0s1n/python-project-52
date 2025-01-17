from django.db import models
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    label = models.CharField(max_length=50, verbose_name=_("name"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    def delete(self, *args, **kwargs):
        if self.task_set.exists():
            raise ProtectedError(
                _("Cannot delete this label because it is being used"),
                self.task_set.all(),
            )
        return super().delete(*args, **kwargs)
