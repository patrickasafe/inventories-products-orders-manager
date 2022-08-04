from apps.inventories.views import InventoryCreateAPIView, InventoryListAPIView, InventoryProductCreateAPIView, InventoryProductListAPIView, InventoryProductMultipleDestroyRequestAPIView, InventoryProductRetrieveUpdateAPIView, InventoryRetrieveUpdateAPIView, InventoryMultipleDestroyRequestAPIView
from django.urls import path

app_name = "inventories"
urlpatterns = [

    # Inventory
    path('', InventoryCreateAPIView.as_view(), name='create_inventory'),
    path('list/', InventoryListAPIView.as_view(), name='list_inventories'),
    path('<int:pk>', InventoryRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_inventory'),
    path('delete-request/', InventoryMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_inventories'),

    # InventoryProduct
    path('inventory-product/', InventoryProductCreateAPIView.as_view(),
         name='create_inventory_product'),
    path('inventory-product/list/', InventoryProductListAPIView.as_view(),
         name='list_inventories_products'),
    path('inventory-product/<int:pk>', InventoryProductRetrieveUpdateAPIView.as_view(),
         name='get_update_delete_inventory_product'),
    path('inventory-product/delete-request/', InventoryProductMultipleDestroyRequestAPIView.as_view(),
         name='destroy_multiple_inventories_products'),

]
