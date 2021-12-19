from django.contrib import admin
from .models import Order, OrderItem, ShippingDetails


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem

    readonly_fields = ('item_total',
                       'vendor_amount',
                       'liffey_amount')

    list_display = (
        'buyer',
        'item',
        'quantity',
        'item_total',
        'vendor_amount',
        'liffey_amount',
        'ordered',
        'vendor_paid',
        'related_order',
    )


class ShippingDetailsAdmin(admin.TabularInline):
    model = ShippingDetails

    list_display = (
        'full_name'
        'address1',
        'address2',
        'city',
        'state',
        'zipcode',
        'country',
    )


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_num',
        'create_date',
        'order_date',
        'grand_total',
        'stripe_pid',
    )

    inlines = (OrderItemAdmin, ShippingDetailsAdmin)

    list_display = (
        'order_num',
        'create_date',
        'order_date',
        'ordered',
    )

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
