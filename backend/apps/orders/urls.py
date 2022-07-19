from apps.orders.views import OrderCreate, OrderList, OrderDetail, OrderDeleteRequest
from django.urls import path

urlpatterns = [
    path('', OrderCreate.as_view()),
    path('list/', OrderList.as_view()),
    path('<int:pk>', OrderDetail.as_view()),
    path('delete-request/', OrderDeleteRequest.as_view())

]
