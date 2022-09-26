from apps.orders.factories import SellingOrderProductFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'selling_inventory_product_relation'
    created_object_plural = 'selling_inventory_product_relations'
    default_quantity = 10
    Factory = SellingOrderProductFactory
