import factory
import json
from django.test import TestCase
from django.urls import reverse

from apps.products.models import Supplier, Product

from apps.products.factories import ProductFactory, SupplierFactory


class TestSupplier(TestCase):

    def setUp(self):

        self.Factory = SupplierFactory
        self.supplier_01 = self.Factory(id=1)
        self.supplier_02 = self.Factory(id=2)

        self.create_url = reverse('products:create_supplier')
        self.list_url = reverse('products:list_suppliers')
        self.get_update_delete_url = reverse(
            'products:get_update_delete_supplier', kwargs={'pk': self.supplier_01.id})

    def test_list(self):
        response = self.client.get(self.list_url)

        self.assertContains(response, 1)
        self.assertContains(response, 2)
        self.assertEquals(Supplier.objects.count(), 2)

    def test_detail(self):

        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = {'id': self.supplier_01.id, "name": self.supplier_01.name, "phone": self.supplier_01.phone,
                   "email": self.supplier_01.email}
        self.assertEquals(data, content)

    def test_create(self):

        supplier = content = factory.build(dict, FACTORY_CLASS=SupplierFactory)
        response = self.client.post(self.create_url, supplier)
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(data, content)
        self.assertEquals(Supplier.objects.count(), 3)

    # TODO WRITE A METHOD TO TEST SOFTDELETE
    # def test_delete(self):

    #     response = self.client.delete(self.read_update_delete_url)
    #     self.assertEquals(response.status_code, 204)
    #     self.assertEquals(Supplier.objects.count(), 1)


class TestProduct(TestCase):

    def setUp(self):

        self.Factory = ProductFactory
        self.supplier_01 = SupplierFactory(id=1)
        self.product_01 = self.Factory(id=1, supplier=self.supplier_01)
        self.product_02 = self.Factory(id=2, supplier=self.supplier_01)

        self.create_url = reverse('products:create_product')
        self.list_url = reverse('products:list_products')
        self.get_update_delete_url = reverse(
            'products:get_update_delete_product', kwargs={'pk': self.product_01.id})

    def test_list(self):
        response = self.client.get(self.list_url)

        self.assertContains(response, "RAN")
        self.assertContains(response, "RAN")
        self.assertEquals(Product.objects.count(), 2)

    def test_detail(self):

        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = {'id': self.product_01.id, "name": self.product_01.name, "ref": self.product_01.ref,
                   "cost": self.product_01.cost, "price": self.product_01.price, "supplier": self.supplier_01.id}
        self.assertEquals(data, content)

    # # # TODO: FIX TEST -> error: Cannot encode None for key 'deleted_at' as POST data. Did you mean to pass an empty string or omit the value?
    # def test_create(self):

    #     product = content = factory.build(dict, FACTORY_CLASS=self.Factory)
    #     response = self.client.post(self.create_url, product)
    #     data = json.loads(response.content)
    #     self.assertEquals(response.status_code, 201)
    #     self.assertEquals(data, content)
    #     self.assertEquals(Product.objects.count(), 3)
