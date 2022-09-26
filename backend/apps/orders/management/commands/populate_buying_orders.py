from apps.orders.factories import BuyingOrderFactory
from apps.common.service.custom_command_base import CustomBaseCommand


class Command(CustomBaseCommand):

    created_object = 'buying_order'
    created_object_plural = 'buying_orders'
    default_quantity = 1000
    Factory = BuyingOrderFactory
