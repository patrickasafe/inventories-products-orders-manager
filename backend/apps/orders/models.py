from django.db import models

from apps.common.models import TimeStampedModel
from apps.products.models import Product


class BuyingOrder(TimeStampedModel):
    """A model class for Orders to inventory replenishment."""

    order_date = models.DateTimeField(verbose_name='Order Date')
    shipment_date = models.DateTimeField(
        null=True, blank=True, verbose_name='Shipment Date')
    products = models.ManyToManyField(
        Product, related_name='buying_orders', through='BuyingOrderProduct', verbose_name='Products')

    def __str__(self):
        return str(self.id)

class SellingOrder(TimeStampedModel):
    """A model class for Orders to inventory replenishment."""

    # customer = models.ForeignKey(User, on_delete=models.CASCADE,
    #                             verbose_name='Customer', related_name='selling_orders' )
    order_date = models.DateTimeField(verbose_name='Order Date')
    shipment_date = models.DateTimeField(
        null=True, blank=True, verbose_name='Shipment Date')
    products = models.ManyToManyField(
        Product, related_name='selling_orders', through='SellingOrderProduct', verbose_name='Products')

    def __str__(self):
        return str(self.id)


class BuyingOrderProduct(TimeStampedModel):
    """A model class for Products and Quantities inside a Order."""

    buying_order = models.ForeignKey(BuyingOrder, on_delete=models.CASCADE,
                              verbose_name='Order', related_name='buying_order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Product', related_name='buying_order_product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Buying Order')

class SellingOrderProduct(TimeStampedModel):
    """A model class for Products and Quantities inside a Order."""

    selling_order = models.ForeignKey(SellingOrder, on_delete=models.CASCADE,
                              verbose_name='Order', related_name='selling_order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Product', related_name='selling_order_product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Selling Order')
        