from rest_framework import generics

from apps.common.views import CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.orders.serializer import OrderProductSerializer, OrderSerializer
from apps.orders.models import Order, OrderProduct


# Order
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# OrderProduct
class OrderProductListAPIView(generics.ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductCreateAPIView(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductMultipleDestroyRequestAPIView(CustomMultipleDestroyRequestAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductSoftDeleteAPIView(CustomSoftDeleteAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderProductRetrieveUpdateAPIView(CustomRetrieveUpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
