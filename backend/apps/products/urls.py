from apps.products.views import ProductCreateAPIView, ProductListAPIView, ProductRetrieveUpdateAPIView, ProductMultipleDestroyRequestAPIView, SupplierCreateAPIView, SupplierListAPIView, SupplierMultipleDestroyRequestAPIView, SupplierRetrieveUpdateAPIView
from django.urls import path

app_name = "products"

urlpatterns = [
    # PRODUCTS URLS
    path('', ProductCreateAPIView.as_view(), name='create_product'),
    path('list/', ProductListAPIView.as_view(), name='list_products'),
    path('<int:pk>', ProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_product'),
    path('delete_request/', ProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_products'),
    # SUPPLIERS URLS
    path('suppliers/', SupplierCreateAPIView.as_view(), name='create_supplier'),
    path('suppliers/list/', SupplierListAPIView.as_view(),
         name='list_suppliers'),
    path('suppliers/<int:pk>', SupplierRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_supplier'),
    path('suppliers/delete-request/', SupplierMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_suppliers'),

]
