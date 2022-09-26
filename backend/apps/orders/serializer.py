from rest_framework import serializers
from apps.orders.models import BuyingOrder, SellingOrder, BuyingOrderProduct,  SellingOrderProduct


class BuyingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingOrder
        fields = ["id", "order_date", "shipment_date", "products"]

class SellingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingOrder
        fields = ["id", "order_date", "shipment_date", "products"]


class BuyingOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingOrderProduct
        fields = ["id", "buying_order", "product", "quantity"]

class SellingOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingOrderProduct
        fields = ["id", "selling_order", "product", "quantity"]