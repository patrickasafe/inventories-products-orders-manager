import factory
import factory.fuzzy

from .common.factories_utils_configs import fruits_adjectives, fruits_names, suppliers_names, suppliers_ajectives

from .common.factories import FactoryUtils

from . import models


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Supplier

    name = factory.fuzzy.FuzzyChoice(
        choices=FactoryUtils.random_name_generator(suppliers_names, suppliers_ajectives))
    phone = factory.Sequence(lambda n: "+552198%07d" % n)
    email = factory.faker.Faker('email')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = factory.fuzzy.FuzzyChoice(
        choices=FactoryUtils.random_name_generator(fruits_names, fruits_adjectives))
    ref = factory.Sequence(lambda n: "RAN%06d" % n)
    cost = factory.fuzzy.FuzzyFloat(1, 50, 2)
    price = factory.fuzzy.FuzzyFloat(51, 100, 2)
    supplier = factory.SubFactory(SupplierFactory)


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Inventory

    name = factory.Sequence(lambda n: "Loja %03d" % n)
    ref = factory.Sequence(lambda n: "RAN%06d" % n)
    address = factory.faker.Faker('address')
    