from django.db import models

from apps.common.models import TimeStampedModel
from apps.products.models import Product


class Order(TimeStampedModel):
    """A model class for Orders to inventory replenishment."""

    date_order = models.DateTimeField(verbose_name='Order Date')
    date_shipment = models.DateTimeField(
        null=True, blank=True, verbose_name='Shipment Date')
    products = models.ManyToManyField(
        Product, related_name='orders', through='OrderProduct', verbose_name='Products')

    def __str__(self):
        return str(self.id)


class OrderProduct(TimeStampedModel):
    """A model class for Inventories."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Order', related_name='order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Product', related_name='order_product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Order')
