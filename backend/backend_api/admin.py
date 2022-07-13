from django.contrib import admin
from backend_api.models import Product, Inventory, InventoryProduct, Supplier

class Suppliers(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'cost', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Inventories(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class ProductsInventories(admin.ModelAdmin):
    list_display = ('inventory', 'product', 'quantity')
    # list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Supplier, Suppliers)
admin.site.register(Product, Products)
admin.site.register(Inventory, Inventories)
admin.site.register(InventoryProduct, ProductsInventories)
