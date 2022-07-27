from apps.inventories.views import InventoryCreateAPIView, InventoryListAPIView, InventoryRetrieveUpdateAPIView, InventoryMultipleDestroyRequestAPIView
from django.urls import path

urlpatterns = [
    path('', InventoryCreateAPIView.as_view()),
    path('list/', InventoryListAPIView.as_view()),
    path('<int:pk>', InventoryRetrieveUpdateAPIView.as_view()),
    path('delete-request/', InventoryMultipleDestroyRequestAPIView.as_view())

]
