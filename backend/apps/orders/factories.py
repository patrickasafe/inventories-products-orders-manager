import factory
from factory import fuzzy

from apps.common.factories import FactoryUtils

from . import models


class BuyingOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BuyingOrder

    order_date = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))
    shipment_date = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))

class SellingOrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SellingOrder

    order_date = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))
    shipment_date = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))


class BuyingOrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BuyingOrderProduct

    buying_order = factory.Iterator(models.BuyingOrder.objects.all())
    product = factory.Iterator(models.Product.objects.all())
    quantity = fuzzy.FuzzyInteger(10, 200, 5)

class SellingOrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SellingOrderProduct

    selling_order = factory.Iterator(models.SellingOrder.objects.all())
    product = factory.Iterator(models.Product.objects.all())
    quantity = fuzzy.FuzzyInteger(10, 200, 5)