import factory
from factory import fuzzy

from apps.common.factories import FactoryUtils

from . import models


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    date_order = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))
    date_shipment = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))


class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.OrderProduct

    order = factory.Iterator(models.Order.objects.all())
    product = factory.Iterator(models.Product.objects.all())
    quantity = fuzzy.FuzzyInteger(10, 200, 5)
