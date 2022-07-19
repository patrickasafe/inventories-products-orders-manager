import factory
from factory import fuzzy

from . import models


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Inventory

    name = factory.Sequence(lambda n: "Estoque %03d" % n)
    ref = factory.Sequence(lambda n: "RAN%03d" % n)
    address = factory.faker.Faker('address')


class InventoryProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.InventoryProduct

    inventory = factory.Iterator(models.Inventory.objects.all())
    product = factory.Iterator(models.Product.objects.all())
    quantity = fuzzy.FuzzyInteger(10, 200, 5)
