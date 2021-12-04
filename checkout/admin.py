from django.contrib import admin
from .models import Order, OrderItem, BillingAddress


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_num',
        'user',
        'order_date',
        'ordered',
    )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'buyer',
        'item',
        'quantity',
        'ordered',
        'related_order',
    )


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'address1',
        'city',
        'state',
        'zipcode',
        'country',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
