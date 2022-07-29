from apps.orders.views import OrderCreateAPIView, OrderListAPIView, OrderProductCreateAPIView, OrderProductListAPIView, OrderProductMultipleDestroyRequestAPIView, OrderProductRetrieveUpdateAPIView, OrderRetrieveUpdateAPIView, OrderMultipleDestroyRequestAPIView
from django.urls import path

app_name = "orders"
urlpatterns = [

    # ORDER URLs
    path('', OrderCreateAPIView.as_view(), name='create_product'),
    path('list/', OrderListAPIView.as_view(), name='list_products'),
    path('<int:pk>', OrderRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_product'),
    path('delete-request/', OrderMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_products'),

    # ORDER_PRODUCT URLs
    path('order/', OrderProductCreateAPIView.as_view(), name='create_product'),
    path('order/list/', OrderProductListAPIView.as_view(), name='list_products'),
    path('order/<int:pk>', OrderProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_product'),
    path('order/delete-request/', OrderProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_products'),

]
