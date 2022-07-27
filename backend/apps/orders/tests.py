from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status



# class TestEndpoints(APITestCase):

#     def test_should_create_order(self):
#         sample_supplier = {
#             "date_order": "1",
#             "date_shipment": "any",
#             "products": "+5521987650181",
#             "email": "patrickasafe@gmail.com",
#         }

#         response = self.client.post(
#             reverse('create_supplier'), sample_supplier)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_should_create_product(self):
#         sample_product = {
#             "name": "any",
#             "ref": "RAN000001",
#             "cost": 10,
#             "price": 20,
#             "supplier": 1
#         }

#         self.test_should_create_supplier()
#         response = self.client.post(
#             reverse('create_product'), sample_product)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
