from django.contrib import admin
from .models import Order, OrderItem, BillingAddress


class OrderItemAdmin(admin.TabularInline):

    model = OrderItem

    list_display = (
        'buyer',
        'item',
        'quantity',
        'item_total',
        'ordered',
        'related_order',
    )


class OrderAdmin(admin.ModelAdmin):
    
    inlines = (OrderItemAdmin,)
    
    list_display = (
        'order_num',
        'create_date',
        'order_date',
        'ordered',
    )

    ordering = ('-order_date',)


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
admin.site.register(BillingAddress, BillingAddressAdmin)
