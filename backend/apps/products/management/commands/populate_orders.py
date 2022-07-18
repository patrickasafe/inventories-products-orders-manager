from apps.products.factories import OrderFactory
from apps.products.management.commands.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'order'
    created_object_plural = 'orders'
    default_quantity = 1000
    Factory = OrderFactory
