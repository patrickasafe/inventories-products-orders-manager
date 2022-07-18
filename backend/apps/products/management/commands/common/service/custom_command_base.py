from django.core.management.base import BaseCommand, CommandError
from faker import Factory


class CustomBaseCommand(BaseCommand):
    '''An extended Base command reducing redudancy'''

    def __init__(self, *args, **kwargs):
        if Factory is None:
            raise ValueError
        super(CustomBaseCommand, self).__init__(*args, **kwargs)

    created_object = ''
    created_object_plural = ''
    default_quantity = 0  # TODO EDIT default_quantity used when no quantity is defined
    Factory = None

    help = f'Populates DataBase {created_object_plural.capitalize()} table'

    def make_objects(self, quantity=0):
        if quantity <= 0:
            raise ValueError
        for _ in range(quantity):
            self.Factory()

    def add_arguments(self, parser):  # TODO EDIT quantity as optional argment
        parser.add_argument('quantity', nargs='+', type=int)

    def handle(self, *args, **options):
        for quantity in options['quantity']:
            try:
                self.make_objects(quantity)
            except:
                raise CommandError(
                    f'Could not create {self.created_object_plural}')
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created {quantity} {self.created_object_plural}'))
