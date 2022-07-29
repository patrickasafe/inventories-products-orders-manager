from rest_framework import serializers
from apps.orders.models import Order, OrderProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["date_order", "date_shipment", "products"]


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["date_order", "date_shipment", "products"]
