from django.contrib import admin

from apps.inventories.models import Inventory, InventoryProduct


class Inventories(admin.ModelAdmin):
    list_display = ('id', 'name', 'ref', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


class InventoriesProducts(admin.ModelAdmin):
    list_display = ('inventory', 'product', 'quantity')
    list_display_links = ('inventory', 'product')
    list_per_page = 20


admin.site.register(Inventory, Inventories)
admin.site.register(InventoryProduct, InventoriesProducts)
