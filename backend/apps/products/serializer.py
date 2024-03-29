from rest_framework import serializers
from apps.products.models import Product, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'phone', 'email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'ref', 'cost', 'price', 'supplier']

    #TODO IMPROVE THIS VALIDATION
    def validate(self, data):
        return data

    def get_description(self, data):
        return "This crop is called " + data.name + ", it costs $" + str(data.cost) + " and is sold for $" + (data.price)
