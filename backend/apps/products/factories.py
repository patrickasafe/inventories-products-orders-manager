import factory
from factory import fuzzy

from apps.common.factories import FactoryUtils

from apps.common.configs import FactoryOptions

from . import models


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Supplier

    name = fuzzy.FuzzyChoice(
        choices=FactoryUtils.random_name_generator(FactoryOptions.suppliers_names, FactoryOptions.suppliers_ajectives))
    phone = factory.Sequence(lambda n: "+55219%08d" % n)
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
