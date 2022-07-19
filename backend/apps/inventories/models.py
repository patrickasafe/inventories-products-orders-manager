from django.db import models

from apps.common.models import TimeStampedModel
from apps.products.models import Product


class Inventory(TimeStampedModel):
    """A model class for Inventory information."""

    name = models.CharField(max_length=45, verbose_name='Name')
    ref = models.CharField(max_length=6, verbose_name='Reference')
    address = models.CharField(
        max_length=200, verbose_name='Address')
    products = models.ManyToManyField(Product,
                                      related_name='inventories', through="InventoryProduct", verbose_name='Products')

    def __str__(self):
        return str(self.id)


class InventoryProduct(TimeStampedModel):
    """A model class for Inventories."""

    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE,
                                  verbose_name='Inventory', related_name='inventory_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='inventory_product', verbose_name='Product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Inventory')
