from apps.inventories.factories import InventoryFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'inventory'
    created_object_plural = 'inventories'
    default_quantity = 5
    Factory = InventoryFactory
