from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

User = get_user_model()


class Task(models.Model):
    name = models.CharField(
        max_length=255, blank=False, unique=True, verbose_name=_("name")
    )
    body = models.TextField(blank=False, verbose_name=_("Description"))
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("Author"),
        related_name=_("Author"),
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name=_("Status")
    )
    performer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name=_("Performer"),
        related_name=_("Performer"),
    )
    labels = models.ManyToManyField(Label, blank=True, verbose_name=_("Labels"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
