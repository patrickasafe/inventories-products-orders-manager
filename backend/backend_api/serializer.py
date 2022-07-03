from django.forms import ValidationError
from rest_framework import serializers
from backend_api.validators import validate_name
from backend_api.models import Product, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, data):
        if not validate_name(data['name']):
            raise serializers.ValidationError(
                {'name': 'The name must not contain numbers'})
        return data

    def get_description(self, data):
        return "This crop is called " + data['name'] + ", it costs $" + str(data.cost) + " and is sold for $" + (data.price)

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"