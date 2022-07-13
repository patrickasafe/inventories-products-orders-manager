from django.db import models

from backend_api.common.models import TimeStampedModel


class Supplier(TimeStampedModel):
    """A model class for Supliers."""

    name = models.CharField(max_length=45, verbose_name='Name')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    email = models.CharField(max_length=45, verbose_name='Email')

    def __str__(self):
        return str(self.id)


class Product(TimeStampedModel):
    """A model class for Products."""

    name = models.CharField(max_length=45, verbose_name='Name')
    ref = models.CharField(max_length=9, verbose_name='Reference')
    cost = models.FloatField(verbose_name='Cost Price')
    price = models.FloatField(verbose_name='Selling Price')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 verbose_name='Supplier', related_name='products')

    def __str__(self):
        return str(self.id)


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


class Order(TimeStampedModel):
    """A model class for Orders to inventory replenishment."""

    date_order = models.DateTimeField(auto_now_add=True)
    date_shipment = models.DateTimeField(null=True, blank=True)
    products = models.ManyToManyField(
        Product, related_name='orders', through='OrderProduct', verbose_name='Products')

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


class OrderProduct(TimeStampedModel):
    """A model class for Inventories."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='Order', related_name='order_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Product', related_name='order_product')
    quantity = models.IntegerField(
        verbose_name='Product quantity at Order')
