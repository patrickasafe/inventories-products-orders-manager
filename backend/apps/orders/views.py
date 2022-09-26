from rest_framework import generics

from apps.common.views import CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.orders.serializer import BuyingOrderProductSerializer, BuyingOrderSerializer, SellingOrderProductSerializer, SellingOrderSerializer
from apps.orders.models import BuyingOrder, BuyingOrderProduct, SellingOrder, SellingOrderProduct


# BuyingOrderViews
class BuyingOrderListAPIView(generics.ListAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class BuyingOrderCreateAPIView(generics.CreateAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class BuyingOrderMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class BuyingOrderSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class BuyingOrderRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


# SellingOrderViews
class SellingOrderListAPIView(generics.ListAPIView):
    queryset = SellingOrder.objects.all()
    serializer_class = SellingOrderSerializer


class SellingOrderCreateAPIView(generics.CreateAPIView):
    queryset = SellingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class SellingOrderMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = SellingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class SellingOrderSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = SellingOrder.objects.all()
    serializer_class = BuyingOrderSerializer


class SellingOrderRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = BuyingOrder.objects.all()
    serializer_class = BuyingOrderSerializer

# BuyingOrderProductViews
class BuyingOrderProductListAPIView(generics.ListAPIView):
    queryset = BuyingOrderProduct.objects.all()
    serializer_class = BuyingOrderProductSerializer


class BuyingOrderProductCreateAPIView(generics.CreateAPIView):
    queryset = BuyingOrderProduct.objects.all()
    serializer_class = BuyingOrderProductSerializer


class BuyingOrderProductMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = BuyingOrderProduct.objects.all()
    serializer_class = BuyingOrderProductSerializer


class BuyingOrderProductSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = BuyingOrderProduct.objects.all()
    serializer_class = BuyingOrderProductSerializer


class BuyingOrderProductRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = BuyingOrderProduct.objects.all()
    serializer_class = BuyingOrderProductSerializer

# SellingOrderProductViews
class SellingOrderProductListAPIView(generics.ListAPIView):
    queryset = SellingOrderProduct.objects.all()
    serializer_class = SellingOrderProductSerializer


class SellingOrderProductCreateAPIView(generics.CreateAPIView):
    queryset = SellingOrderProduct.objects.all()
    serializer_class = SellingOrderProductSerializer


class SellingOrderProductMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = SellingOrderProduct.objects.all()
    serializer_class = SellingOrderProductSerializer


class SellingOrderProductSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = SellingOrderProduct.objects.all()
    serializer_class = SellingOrderProductSerializer


class SellingOrderProductRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = SellingOrderProduct.objects.all()
    serializer_class = SellingOrderProductSerializer
