from apps.orders.factories import SellingOrderFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'selling_order'
    created_object_plural = 'selling_orders'
    default_quantity = 1000
    Factory = SellingOrderFactory
