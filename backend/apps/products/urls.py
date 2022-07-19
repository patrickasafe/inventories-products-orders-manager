from apps.products.views import ProductCreate, ProductList, ProductDetail, ProductDeleteRequest
from django.urls import path

urlpatterns = [
    path('', ProductCreate.as_view()),
    path('list/', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('delete-request/', ProductDeleteRequest.as_view())

]
