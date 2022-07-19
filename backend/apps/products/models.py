from django.db import models

from apps.common.models import TimeStampedModel


class Supplier(TimeStampedModel):
    """A model class for Supliers."""

    name = models.CharField(max_length=45, verbose_name='Name')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    email = models.CharField(max_length=45, verbose_name='Email')

    def __str__(self):
        return str(self.id)


class Product(TimeStampedModel):
    """A model class for apps.products."""

    name = models.CharField(max_length=45, verbose_name='Name')
    ref = models.CharField(max_length=9, verbose_name='Reference')
    cost = models.FloatField(verbose_name='Cost Price')
    price = models.FloatField(verbose_name='Selling Price')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 verbose_name='Supplier', related_name='products')

    def __str__(self):
        return str(self.id)
