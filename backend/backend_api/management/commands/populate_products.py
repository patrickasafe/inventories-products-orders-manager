# import string

# from django.core.management.base import BaseCommand, CommandError

# from faker import Faker

# from backend_api.models import Product
# from backend_api.management.commands.common.service.generator import Generator


# class Command(BaseCommand, Generator):
#     '''Populates the DB'''

#     help = 'Populates DataBase products table'

#     def add_arguments(self, parser):
#         parser.add_argument('products_quantity', nargs='+', type=int)

#     def handle(self, *args, **options):
#         for products_quantity in options['products_quantity']:
#             try:
#                 self.create_products(products_quantity)
#             except:
#                 raise CommandError('Could not create products')

#             self.stdout.write(self.style.SUCCESS(
#                 'Successfully created "%s" products' % products_quantity))

#     def create_products(self, products_quantity):
#         Faker.seed(10)
#         for _ in range(products_quantity):
#             name = self.random_product_name_generator()
#             ref = '{}{}'.format(self.random_string_generator(3, string.ascii_uppercase),
#                                 self.random_string_generator(6, string.digits))
#             cost = '{}'.format(self.random_float_generator(1, 99, 2))
#             price = '{}'.format(self.random_float_generator(101, 199, 2))
#             deleted_at = None
#             p = Product(name=name, ref=ref, cost=cost,
#                         price=price, deleted_at=deleted_at)
#             p.save()

from django.core.management.base import BaseCommand, CommandError

from faker import Faker
from backend_api import factories


class Command(BaseCommand):
    '''Populates the DB with Products'''

    help = 'Populates DataBase Products table'

    def add_arguments(self, parser):
        parser.add_argument('quantity', nargs='+', type=int)

    def handle(self, *args, **options):
        for quantity in options['quantity']:
            try:
                self.make_objects(quantity)
            except:
                raise CommandError('Could not create products')

            self.stdout.write(self.style.SUCCESS(
                'Successfully created "%s" products' % quantity))

    def make_objects(self, quantity=150):
        Faker.seed(10)
        products = []

        products.extend(
            factories.ProductFactory.create_batch(quantity))
