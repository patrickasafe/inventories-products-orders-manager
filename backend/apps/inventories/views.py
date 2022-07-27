from rest_framework import generics

from apps.common.views import  CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.inventories.serializer import InventorySerializer
from apps.inventories.models import Inventory


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
