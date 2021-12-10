import json
import time
from django.http import HttpResponse

from product.models import Product
from checkout.models import Order, OrderItem


class StripeWH_Handler:
    """
    Functions to handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Generic webhook handler
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handler for payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.pid
        cart = intent.metadata.cart
        save_defaults = intent.metadata.save_defaults

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.charges.data[0].shipping_details
        grand_total = round(intent.data.charges[0].amount /100, 2)        

        # Clean up shipping details data coming from Stripe
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Assume order does not exist yet, check for existing order
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Order exists in database.',
                    status=200,
                )
        else:
            try:   
                # Create new order in DB using form details passed from Stripe
                order = Order.objects.create(
                        stripe_pid=pid,
                    )
                # Loop through cart provided in metadata to add order items
                for sku, item_data in json.load(cart).items():
                    product = Product.objects.get(sku=sku)
                    order_item = OrderItem(
                        related_order=order,
                        buyer=self.request.user,
                        item=product,
                        quantity=item_data,
                        ordered=True,
                    )
                    order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created in webhook.',
            status=200,
        )

    def handle_payment_intent_failed(self, event):
        """
        Handler for payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )