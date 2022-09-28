import factory
import json

from rest_framework.test import APITestCase

from django.urls import reverse

from apps.common.test_utils import TestCustomUtils

from apps.orders.models import Order, OrderProduct
from apps.orders.factories import OrderFactory, OrderProductFactory

from apps.products.factories import ProductFactory, SupplierFactory

# TODO: REWRITE TESTS FOR NEW TABLES: 
order_create_url = reverse('orders:create_order')
order_list_url = reverse('orders:list_orders')
order_product_create_url = reverse('orders:create_order_product')
order_product_list_url = reverse('orders:list_orders_products')


# TODO: WRITE A METHOD TO TEST SOFTDELETE
# TODO: WRITE A METHOD TO TEST UPDATE
class TestOrder(APITestCase):

    def setUp(self):
        self.Factory = OrderFactory

        self.data_order_01 = factory.build(dict, FACTORY_CLASS=self.Factory)
        self.order_01 = self.Factory(**self.data_order_01)

        self.data_order_02 = factory.build(dict, FACTORY_CLASS=self.Factory)
        self.order_02 = self.Factory(**self.data_order_02)

        self.get_update_delete_url = reverse(
            'orders:get_update_delete_order', kwargs={'pk': self.order_01.id})

    # TODO: create a convert_date_from_factory_format_to_response_format function. Can you imagine what does is do??
    def test_list(self):
        response = self.client.get(order_list_url)
        data = json.loads(response.content)
        # assert self.order_01['ship'] in str(data)
        # assert self.order_02['ship'] in str(data)
        assert Order.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_order_01
        TestCustomUtils.fix_id_assertion(data, content)
        # NOTE: this assertion is necessary, because factoryboy return different date format from DB response date format
        TestCustomUtils.fix_fk_assertion(
            data, content, ["date_shipment", "date_order", "products"])
        assert data == content

    def test_create(self):
        order = content = factory.build(dict, FACTORY_CLASS=OrderFactory)
        response = self.client.post(order_create_url, order)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        # NOTE: this assertion is necessary, because factoryboy return different date format from DB response date format
        TestCustomUtils.fix_fk_assertion(
            data, content, ["date_shipment", "date_order", "products"])
        assert response.status_code == 201
        assert data == content


class TestOrderProduct(APITestCase):

    def setUp(self):

        self.Factory = OrderProductFactory

        self.supplier = SupplierFactory()

        self.product = ProductFactory(supplier=self.supplier)

        self.order = OrderFactory()

        self.data_order_product_01 = factory.build(
            dict, FACTORY_CLASS=self.Factory, order=self.order, product=self.product)
        self.order_product_01 = self.Factory(**self.data_order_product_01)

        self.data_order_product_02 = factory.build(
            dict, FACTORY_CLASS=self.Factory, order=self.order, product=self.product)
        self.order_product_02 = self.Factory(**self.data_order_product_02)

        self.get_update_delete_url = reverse(
            'orders:get_update_delete_order_product', kwargs={'pk': self.order_product_01.id})

    # TODO: create a convert_date_from_factory_format_to_response_format function. Can you imagine what does is do??
    def test_list(self):
        # response = self.client.get(order_product_list_url)
        # data = json.loads(response.content)
        # assert self.order_01['ship'] in str(data)
        # assert self.order_02['ship'] in str(data)
        assert OrderProduct.objects.count() == 2

    def test_detail(self):
        response = self.client.get(self.get_update_delete_url)
        data = json.loads(response.content)
        content = self.data_order_product_01
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(data, content, ['order', 'product'])
        assert data == content

    def test_create(self):
        order_product = content = factory.build(
            dict, FACTORY_CLASS=self.Factory, order=self.order, product=self.product)
        response = self.client.post(order_product_create_url, order_product)
        data = json.loads(response.content)
        TestCustomUtils.fix_id_assertion(data, content)
        TestCustomUtils.fix_fk_assertion(data, content, ["order", "product"])
        assert response.status_code == 201
        assert data == content
