import factory
import json

from rest_framework.test import APITestCase

from django.urls import reverse

from apps.common.test_utils import TestCustomUtils

from apps.inventories.models import Inventory, InventoryProduct
from apps.inventories.factories import InventoryFactory, InventoryProductFactory

from apps.products.factories import ProductFactory, SupplierFactory


inventory_create_url = reverse('inventories:create_inventory')
inventory_list_url = reverse('inventories:list_inventories')
inventory_product_create_url = reverse('inventories:create_inventory_product')
inventory_product_list_url = reverse('inventories:list_inventories_products')


# TODO: WRITE A METHOD TO TEST SOFTDELETE
# TODO: WRITE A METHOD TO TEST UPDATE
class TestInventory(APITestCase):

    def setUp(self):
        self.supplier = SupplierFactory()

        self.product = ProductFactory(supplier=self.supplier)

        self.Factory = InventoryFactory

        self.data_inventory_01 = factory.build(
            dict, FACTORY_CLASS=self.Factory)
        self.inventory_01 = self.Factory(**self.data_inventory_01)

        self.data_inventory_02 = factory.build(
            dict, FACTORY_CLASS=self.Factory)
        self.inventory_02 = self.Factory(**self.data_inventory_02)

        self.get_update_delete_url = reverse(
            'inventories:get_update_delete_inventory', kwargs={'pk': self.inventory_01.id})

    # TODO: create a convert_date_from_factory_format_to_response_format function. Can you imagine what does is do??
    def test_list(self):
        response = self.client.get(inventory_list_url)
        data = json.loads(response.content)
        assert self.data_inventory_01['name'] in str(data)
        assert self.data_inventory_02['name'] in str(data)
        assert Inventory.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_inventory_01
        TestCustomUtils.fix_id_assertion(data, content)
        # NOTE: this assertion is necessary, because factoryboy return different date format from DB response date format
        TestCustomUtils.fix_fk_assertion(
            data, content, ["products"])
        assert data == content

    def test_create(self):
        inventory = content = factory.build(
            dict, FACTORY_CLASS=InventoryFactory)
        response = self.client.post(inventory_create_url, inventory)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        # NOTE: this assertion is necessary, because factoryboy return different date format from DB response date format
        TestCustomUtils.fix_fk_assertion(
            data, content, ["products"])
        assert response.status_code == 201
        assert data == content


class TestInventoryProduct(APITestCase):

    def setUp(self):
        self.supplier = SupplierFactory()

        self.product = ProductFactory(supplier=self.supplier)

        self.inventory = InventoryFactory()

        self.Factory = InventoryProductFactory

        self.data_inventory_product_01 = factory.build(
            dict, FACTORY_CLASS=self.Factory, inventory=self.inventory, product=self.product)
        self.inventory_product_01 = self.Factory(
            **self.data_inventory_product_01)

        self.data_inventory_product_02 = factory.build(
            dict, FACTORY_CLASS=self.Factory, inventory=self.inventory, product=self.product)
        self.inventory_product_02 = self.Factory(
            **self.data_inventory_product_02)

        self.get_update_delete_url = reverse(
            'inventories:get_update_delete_inventory_product', kwargs={'pk': self.inventory_product_01.id})

    # TODO: create a convert_date_from_factory_format_to_response_format function. Can you imagine what does is do??
    def test_list(self):
        response = self.client.get(inventory_product_list_url)
        data = json.loads(response.content)
        assert str(self.data_inventory_product_01['quantity']) in str(data)
        assert str(self.data_inventory_product_02['quantity']) in str(data)
        assert InventoryProduct.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_inventory_product_01
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(
            data, content, ['inventory', 'product'])
        assert data == content

    def test_create(self):
        inventory_product = content = factory.build(
            dict, FACTORY_CLASS=self.Factory, inventory=self.inventory, product=self.product)
        response = self.client.post(
            inventory_product_create_url, inventory_product)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(
            data, content, ["inventory", "product"])
        assert response.status_code == 201
        assert data == content
