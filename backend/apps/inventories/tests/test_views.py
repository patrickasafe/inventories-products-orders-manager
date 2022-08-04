import factory
import json

from rest_framework.test import APITestCase

from django.urls import reverse

from apps.common.test_utils import TestCustomUtils

from apps.products.models import Supplier, Product
from apps.products.factories import ProductFactory, SupplierFactory


supplier_create_url = reverse('products:create_supplier')
supplier_list_url = reverse('products:list_suppliers')
product_create_url = reverse('products:create_product')
product_list_url = reverse('products:list_products')

# TODO: WRITE A METHOD TO TEST SOFTDELETE
# TODO: WRITE A METHOD TO TEST UPDATE
class TestSupplier(APITestCase):

    def setUp(self):
        self.Factory = SupplierFactory
        self.data_supplier_01 = factory.build(dict, FACTORY_CLASS=self.Factory)
        self.supplier_01 = self.Factory(**self.data_supplier_01)
        self.data_supplier_02 = factory.build(dict, FACTORY_CLASS=self.Factory)
        self.supplier_02 = self.Factory(**self.data_supplier_02)

        self.get_update_delete_url = reverse(
            'products:get_update_delete_supplier', kwargs={'pk': self.supplier_01.id})

    def test_list(self):
        response = self.client.get(supplier_list_url)
        data = json.loads(response.content)
        assert self.data_supplier_01['name'] in str(data)
        assert self.data_supplier_02['name'] in str(data)
        assert Supplier.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_supplier_01
        TestCustomUtils.fix_id_assertion(data, content)
        assert data == content

    def test_create(self):
        supplier = content = factory.build(dict, FACTORY_CLASS=SupplierFactory)
        response = self.client.post(supplier_create_url, supplier)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        assert response.status_code == 201
        assert data == content


# TODO: WRITE A METHOD TO TEST SOFTDELETE
# TODO: WRITE A METHOD TO TEST UPDATE
class TestProduct(APITestCase):

    def setUp(self):
        self.Factory = ProductFactory
        self.supplier = SupplierFactory._get_or_create(Supplier)
        self.data_product_01 = factory.build(
            dict, FACTORY_CLASS=self.Factory, supplier=self.supplier)
        self.product_01 = self.Factory(**self.data_product_01)
        self.data_product_02 = factory.build(
            dict, FACTORY_CLASS=self.Factory, supplier=self.supplier)
        self.product_02 = self.Factory(**self.data_product_02)
        self.get_update_delete_url = reverse(
            'products:get_update_delete_product', kwargs={'pk': self.product_01.id})

    def test_list(self):
        response = self.client.get(product_list_url)
        data = json.loads(response.content)
        assert self.data_product_01['name'] in str(data)
        assert self.data_product_02['name'] in str(data)
        assert Product.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_product_01
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(data, content, ["supplier"])
        assert data == content

    def test_create(self):
        product = content = factory.build(
            dict, FACTORY_CLASS=self.Factory, supplier=self.supplier)
        response = self.client.post(product_create_url, product)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(data, content, ["supplier"])
        assert response.status_code == 201
        assert data == content
