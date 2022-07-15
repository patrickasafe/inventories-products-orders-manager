import datetime
import factory
from factory import fuzzy

from backend_api.common.factories import FactoryUtils

from backend_api.common.configs import FactoryOptions

from . import models


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Supplier

    name = fuzzy.FuzzyChoice(
        choices=FactoryUtils.random_name_generator(FactoryOptions.suppliers_names, FactoryOptions.suppliers_ajectives))
    phone = factory.Sequence(lambda n: "+552198%07d" % n)
    email = factory.faker.Faker('email')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = fuzzy.FuzzyChoice(
        choices=FactoryUtils.random_name_generator(FactoryOptions.fruits_names, FactoryOptions.fruits_adjectives))
    ref = factory.Sequence(lambda n: "RAN%06d" % n)
    cost = fuzzy.FuzzyFloat(1, 50, 2)
    price = fuzzy.FuzzyFloat(51, 100, 2)
    supplier = factory.Iterator(models.Supplier.objects.all())


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Inventory

    name = factory.Sequence(lambda n: "Estoque %03d" % n)
    ref = factory.Sequence(lambda n: "RAN%06d" % n)
    address = factory.faker.Faker('address')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Order

    date_order = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))
    date_shipment = fuzzy.FuzzyDateTime(
        FactoryUtils.min_date_time_generator(2017))


class InventoryProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.InventoryProduct

    inventory = factory.Iterator(models.Inventory.objects.all())
    product = factory.Iterator(models.Product.objects.all())
    quantity = fuzzy.FuzzyInteger(10, 200, 5)
