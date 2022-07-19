from django.contrib import admin
from apps.products.models import Product, Supplier


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


admin.site.register(Supplier, Suppliers)
admin.site.register(Product, Products)
