from rest_framework import generics

from apps.common.views import CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.inventories.serializer import InventorySerializer, InventoryProductSerializer
from apps.inventories.models import Inventory, InventoryProduct


# Inventory
class InventoryListAPIView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryCreateAPIView(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventorySoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# InventoryProduct
class InventoryProductListAPIView(generics.ListAPIView):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer


class InventoryProductCreateAPIView(generics.CreateAPIView):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer


class InventoryProductMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer


class InventoryProductSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer


class InventoryProductRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = InventoryProduct.objects.all()
    serializer_class = InventoryProductSerializer
