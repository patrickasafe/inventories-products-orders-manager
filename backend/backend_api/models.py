from django.db import models

from backend_api.managers import SoftDeleteManager


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

# Create your models here.


class Product(TimeStampedModel):
    """
    A class model for Products.
    """
    name = models.CharField(max_length=200, verbose_name='Name')
    ref = models.CharField(max_length=9, verbose_name='Reference')
    cost = models.FloatField(verbose_name='Cost Price')
    price = models.FloatField(verbose_name='Selling Price')

    def __str__(self):
        return str(self.id)

class Stock(TimeStampedModel):
    """
    A class model for Products.
    """
    name = models.CharField(max_length=200, verbose_name='Name')
    ref = models.CharField(max_length=9, verbose_name='Reference')
    address = models.CharField(max_length=200, verbose_name='Address')


    def __str__(self):
        return str(self.id)
