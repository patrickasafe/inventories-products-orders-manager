import factory
import pytest
import json
from django.test import Client, TestCase
from django.urls import reverse

from apps.products.models import Supplier, Product

from apps.products.factories import ProductFactory, SupplierFactory

supplier_create_url = reverse('products:create_supplier')
supplier_list_url = reverse('products:list_suppliers')
product_create_url = reverse('products:create_product')
product_list_url = reverse('products:list_products')


class TestSupplier(TestCase):

    def setUp(self):

        self.Factory = SupplierFactory
        self.supplier_01 = self.Factory(id=1)
        self.supplier_02 = self.Factory(id=2)

        self.get_update_delete_url = reverse(
            'products:get_update_delete_supplier', kwargs={'pk': self.supplier_01.id})

    def test_list(self):
        response = self.client.get(supplier_list_url)

        self.assertContains(response, 1)
        self.assertContains(response, 2)
        self.assertEqual(Supplier.objects.count(), 2)

    def test_detail(self):

        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = {'id': self.supplier_01.id, "name": self.supplier_01.name, "phone": self.supplier_01.phone,
                   "email": self.supplier_01.email}
        self.assertEqual(data, content)

    # TODO: WRITE A CREATE TEST IN PYTEST. I CANNOT TEST INSIDE TESTCASE CLASSE BECAUSE THIS BUG BELOW:
    # https://code.djangoproject.com/ticket/22431
    # def test_create(self):

    #     supplier = content = factory.build(dict, FACTORY_CLASS=SupplierFactory)
    #     response = self.client.post(supplier_create_url, supplier)
    #     data = json.loads(response.content)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(data, content)
    #     self.assertEqual(Supplier.objects.count(), 3)

    # TODO: WRITE A METHOD TO TEST SOFTDELETE
    # def test_delete(self):

    #     response = self.client.delete(self.read_update_delete_url)
    #     self.assertEqual(response.status_code, 204)
    #     self.assertEqual(Supplier.objects.count(), 1)


@pytest.mark.django_db
def test_supplier_create():
    client = Client()
    supplier = content = factory.build(dict, FACTORY_CLASS=SupplierFactory)
    response = client.post(supplier_create_url, supplier)
    data = json.loads(response.content)
    data.pop('id')
    assert response.status_code == 201
    assert data == content


class TestProduct(TestCase):

    def setUp(self):

        self.Factory = ProductFactory
        self.supplier_01 = SupplierFactory(id=1)
        self.product_01 = self.Factory(id=1, supplier=self.supplier_01)
        self.product_02 = self.Factory(id=2, supplier=self.supplier_01)
        self.get_update_delete_url = reverse(
            'products:get_update_delete_product', kwargs={'pk': self.product_01.id})

    def test_list(self):
        response = self.client.get(product_list_url)

        self.assertContains(response, "RAN")
        self.assertContains(response, "RAN")
        self.assertEqual(Product.objects.count(), 2)

    def test_detail(self):

        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = {'id': self.product_01.id, "name": self.product_01.name, "ref": self.product_01.ref,
                   "cost": self.product_01.cost, "price": self.product_01.price, "supplier": self.supplier_01.id}
        self.assertEqual(data, content)

    # TODO: WRITE A CREATE TEST IN PYTEST. I CANNOT TEST INSIDE TESTCASE CLASSE BECAUSE THIS BUG BELOW:
    # https://code.djangoproject.com/ticket/22431
    # def test_create(self):

    #     product = content = factory.build(dict, FACTORY_CLASS=self.Factory)
    #     response = self.client.post(supplier_create_url, product)
    #     data = json.loads(response.content)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(data, content)
    #     self.assertEqual(Product.objects.count(), 3)


# @pytest.mark.django_db
# def test_product_create():
#     client = Client()
#     SupplierFactory._get_or_create(Supplier)
#     product = content = factory.build(dict, FACTORY_CLASS=ProductFactory)
#     response = client.post(product_create_url, product)
#     data = json.loads(response.content)
#     data.pop('id')
#     # data.supplier = content["supplier"]
#     assert response.status_code == 201
#     assert data == content
