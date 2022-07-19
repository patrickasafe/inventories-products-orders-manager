from apps.orders.factories import OrderProductFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'inventory_product_relation'
    created_object_plural = 'inventory_product_relations'
    default_quantity = 10
    Factory = OrderProductFactory
