from apps.products.factories import ProductFactory
from apps.products.management.commands.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'product'
    created_object_plural = 'products'
    default_quantity = 150
    Factory = ProductFactory
