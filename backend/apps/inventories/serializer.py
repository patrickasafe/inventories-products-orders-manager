from rest_framework import serializers
from apps.inventories.models import Inventory, InventoryProduct


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "name", "ref", "address", "products"]


class InventoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryProduct
        fields = ["id", "inventory", "product", "quantity"]
