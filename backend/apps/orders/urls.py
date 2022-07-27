from apps.orders.views import OrderCreateAPIView, OrderListAPIView, OrderRetrieveUpdateAPIView, OrderMultipleDestroyRequestAPIView
from django.urls import path

app_name = "orders"
urlpatterns = [
    path('', OrderCreateAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
    path('<int:pk>', OrderRetrieveUpdateAPIView.as_view()),
    path('delete-request/', OrderMultipleDestroyRequestAPIView.as_view())

]
