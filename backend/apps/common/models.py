from django.db import models

from apps.common.managers import SoftDeleteManager


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides auditing fields.
    ``created_at`` and ``updated_at`` are self-updating fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        null=True,
        db_index=True,
        blank=True,
    )

    objects = SoftDeleteManager()

    class Meta:
        abstract = True
