from apps.orders.views import OrderCreateAPIView, OrderListAPIView, OrderProductCreateAPIView, OrderProductListAPIView, OrderProductMultipleDestroyRequestAPIView, OrderProductRetrieveUpdateAPIView, OrderRetrieveUpdateAPIView, OrderMultipleDestroyRequestAPIView
from django.urls import path

app_name = "orders"
urlpatterns = [

    # ORDER URLs
    path('', OrderCreateAPIView.as_view(), name='create_order'),
    path('list/', OrderListAPIView.as_view(), name='list_orders'),
    path('<int:pk>', OrderRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_order'),
    path('delete-request/', OrderMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_orders'),

    # ORDER_PRODUCT URLs
    path('order-product/', OrderProductCreateAPIView.as_view(),
         name='create_order_product'),
    path('order-product/list/', OrderProductListAPIView.as_view(),
         name='list_orders_products'),
    path('order-product/<int:pk>', OrderProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_order_product'),
    path('order-product/delete-request/', OrderProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_orders_products'),

]
