from django.contrib import admin
from backend_api.models import Order, OrderProduct, Product, Inventory, InventoryProduct, Supplier


class Suppliers(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'cost', 'price', 'supplier')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Inventories(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Orders(admin.ModelAdmin):
    list_display = ('id', 'date_order', 'date_shipment')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


class InventoriesProducts(admin.ModelAdmin):
    list_display = ('inventory', 'product', 'quantity')
    list_display_links = ('inventory', 'product')
    list_per_page = 20


class OrderProducts(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_display_links = ('order', 'product')
    list_per_page = 20


admin.site.register(Supplier, Suppliers)
admin.site.register(Product, Products)
admin.site.register(Inventory, Inventories)
admin.site.register(Order, Orders)
admin.site.register(InventoryProduct, InventoriesProducts)
admin.site.register(OrderProduct, OrderProducts)
