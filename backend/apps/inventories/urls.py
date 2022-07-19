from apps.inventories.views import InventoryCreate, InventoryList, InventoryDetail, InventoryDeleteRequest
from django.urls import path

urlpatterns = [
    path('', InventoryCreate.as_view()),
    path('list/', InventoryList.as_view()),
    path('<int:pk>', InventoryDetail.as_view()),
    path('delete-request/', InventoryDeleteRequest.as_view())

]
