from django.contrib import admin
from backend_api.models import Product, Stock


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'cost', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Stocks(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Product, Products)
admin.site.register(Stock, Stocks)
