import random

from django.core.management.base import BaseCommand, CommandError

from faker import Faker
import faker

from backend_api.models import ProductInventory, Inventory
from backend_api.management.commands.common.service.generator import Generator


class Command(BaseCommand, Generator):
    '''Populates the DB'''

    help = 'Populates DataBase stock and stock_place tables'

    def add_arguments(self, parser):
        parser.add_argument('stocks_quantity', nargs='+', type=int)

    def handle(self, *args, **options):
        for products_quantity in options['stocks_quantity']:
            try:
                self.create_stocks(stocks_quantity)
            except:
                raise CommandError('Could not create products')

            self.stdout.write(self.style.SUCCESS(
                'Successfully created "%s" products' % products_quantity))

    def create_stocks(self, products_quantity):
        Faker.seed(10)
        fake = Faker('pt_br')
        for _ in range(products_quantity):
            name = self.random_product_name_generator()
            ref = '{}{}'.format(self.random_string_generator(3),
                                random.randrange(000000, 999999))
            cost = '{}'.format(self.random_float_generator(1, 99, 2))
            price = '{}'.format(self.random_float_generator(101, 199, 2))
            deleted_at = None
            p = ProductInventory(name=name, ref=ref, cost=cost,
                                 price=price, deleted_at=deleted_at)
            p.save()
