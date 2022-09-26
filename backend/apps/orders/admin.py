from django.contrib import admin

from apps.orders.models import BuyingOrder, BuyingOrderProduct, SellingOrder, SellingOrderProduct


class BuyingOrders(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'shipment_date')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


class SellingOrders(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'shipment_date')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


class BuyingOrderProducts(admin.ModelAdmin):
    list_display = ('buying_order', 'product', 'quantity')
    list_display_links = ('buying_order', 'product')
    list_per_page = 20


class SellingOrderProducts(admin.ModelAdmin):
    list_display = ('selling_order', 'product', 'quantity')
    list_display_links = ('selling_order', 'product')
    list_per_page = 20


admin.site.register(BuyingOrder, BuyingOrders)

admin.site.register(SellingOrder, SellingOrders)


admin.site.register(BuyingOrderProduct, BuyingOrderProducts)

admin.site.register(SellingOrderProduct, SellingOrderProducts)
