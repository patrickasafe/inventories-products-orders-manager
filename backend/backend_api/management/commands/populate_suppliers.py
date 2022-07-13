from backend_api.factories import SupplierFactory
from backend_api.management.commands.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'supplier'
    created_object_plural = 'suppliers'
    default_quantity = 10
    Factory = SupplierFactory
