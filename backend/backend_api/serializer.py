from django.forms import ValidationError
from rest_framework import serializers
from backend_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate_name(self, data):

        ##NEED TO FIX THIS LATER :)
        # if data["name"] == "Cannabis": # or "Poppy plant":
            # raise ValidationError("Too bad, we only sell legalized crops")
        return data

    def get_description(self, data):
        return "This crop is called " + data.name + ", it costs $" + str(data.cost) + " and is sold for $" + (data.price)
