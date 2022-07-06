from django.contrib import admin
from backend_api.models import Product, StockPlace, Stock


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'cost', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class StocksPlaces(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class Stocks(admin.ModelAdmin):
    list_display = ('id', 'stock_place', 'quantity')
    list_display_links = ('id', 'quantity')
    list_per_page = 20


admin.site.register(Product, Products)
admin.site.register(StockPlace, StocksPlaces)
admin.site.register(Stock, Stocks)
