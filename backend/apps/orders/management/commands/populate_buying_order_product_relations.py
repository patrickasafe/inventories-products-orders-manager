from apps.orders.factories import BuyingOrderProductFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'buying_inventory_product_relation'
    created_object_plural = 'buying_inventory_product_relations'
    default_quantity = 10
    Factory = BuyingOrderProductFactory
