from django.db import models

from .common.models import TimeStampedModel


class Product(TimeStampedModel):
    """A class model for Products."""

    name = models.CharField(max_length=200, verbose_name='Name')
    ref = models.CharField(max_length=9, verbose_name='Reference')
    cost = models.FloatField(verbose_name='Cost Price')
    price = models.FloatField(verbose_name='Selling Price')

    def __str__(self):
        return str(self.id)


class Inventory(TimeStampedModel):
    """A class model for Stock Place."""

    name = models.CharField(max_length=200, verbose_name='Name')
    ref = models.CharField(max_length=6, verbose_name='Reference')
    address = models.CharField(
        max_length=200, verbose_name='Address')
    products = models.ManyToManyField(Product,
                                      related_name='inventories', through="ProductInventory", verbose_name='Products')

    def __str__(self):
        return str(self.id)


class ProductInventory(TimeStampedModel):
    """A class model for Stock."""
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE,
                                  verbose_name='Inventory', related_name='product_inventory')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_inventory', verbose_name='Product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Inventory')
