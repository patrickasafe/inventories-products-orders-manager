from django.contrib import admin

from apps.orders.models import Order, OrderProduct


class Orders(admin.ModelAdmin):
    list_display = ('id', 'date_order', 'date_shipment')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20


class OrderProducts(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_display_links = ('order', 'product')
    list_per_page = 20


admin.site.register(Order, Orders)

admin.site.register(OrderProduct, OrderProducts)
