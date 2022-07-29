from rest_framework import generics

from apps.common.views import CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.products.models import Product, Supplier
from apps.products.serializer import ProductSerializer, SupplierSerializer

# Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Supplier
class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
