from rest_framework import generics

from apps.common.views import CustomMultipleDestroyRequestAPIView, CustomRetrieveUpdateAPIView, CustomSoftDeleteAPIView

from apps.orders.serializer import OrderSerializer
from apps.orders.models import Order


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
