from django.core.management.base import BaseCommand, CommandError


class CustomBaseCommand(BaseCommand):
    '''An extended Base command reducing redudancy'''

    class EmptyClass:
        pass

    created_object = ''
    created_object_plural = ''
    default_quantity = 0
    Factory = EmptyClass

    help = f'Populates DataBase {created_object_plural.capitalize()} table'

    def make_objects(self, quantity: int = default_quantity):
        for _ in range(quantity):
            self.Factory()

    def add_arguments(self, parser):
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
