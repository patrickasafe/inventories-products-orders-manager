from apps.orders.views import BuyingOrderCreateAPIView, BuyingOrderListAPIView, BuyingOrderMultipleDestroyRequestAPIView, BuyingOrderProductCreateAPIView, BuyingOrderProductListAPIView, BuyingOrderProductMultipleDestroyRequestAPIView, BuyingOrderProductRetrieveUpdateAPIView, BuyingOrderRetrieveUpdateAPIView, SellingOrderCreateAPIView, SellingOrderListAPIView, SellingOrderMultipleDestroyRequestAPIView, SellingOrderProductCreateAPIView, SellingOrderProductListAPIView, SellingOrderProductMultipleDestroyRequestAPIView, SellingOrderProductRetrieveUpdateAPIView, SellingOrderRetrieveUpdateAPIView
from django.urls import path

app_name = "orders"
urlpatterns = [

    # BUYING_ORDER URLs
    path('buying/', BuyingOrderCreateAPIView.as_view(),
         name='create_buying_order'),
    path('buying/list/', BuyingOrderListAPIView.as_view(),
         name='list_buying_orders'),
    path('buying/<int:pk>', BuyingOrderRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_buying_order'),
    path('buying/delete-request/', BuyingOrderMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_buying_orders'),

    # SELLING_ORDER URLs
    path('selling/', SellingOrderCreateAPIView.as_view(),
         name='create_selling_order'),
    path('selling/list/', SellingOrderListAPIView.as_view(),
         name='list_selling_orders'),
    path('selling/<int:pk>', SellingOrderRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_selling_order'),
    path('selling/delete-request/', SellingOrderMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_selling_orders'),

    # BUYING_ORDER_PRODUCT URLs
    path('buying/order-product/', BuyingOrderProductCreateAPIView.as_view(),
         name='create_buying_order_product'),
    path('buying/order-product/list/', BuyingOrderProductListAPIView.as_view(),
         name='list_buying_orders_products'),
    path('buying/order-product/<int:pk>', BuyingOrderProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_buying_order_product'),
    path('buying/order-product/delete-request/', BuyingOrderProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_buying_orders_products'),

    # SELLING_ORDER_PRODUCT URLs
    path('selling/order-product/', SellingOrderProductCreateAPIView.as_view(),
         name='create_selling_order_product'),
    path('selling/order-product/list/', SellingOrderProductListAPIView.as_view(),
         name='list_selling_orders_products'),
    path('selling/order-product/<int:pk>', SellingOrderProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_selling_order_product'),
    path('selling/order-product/delete-request/', SellingOrderProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_selling_orders_products'),

]
