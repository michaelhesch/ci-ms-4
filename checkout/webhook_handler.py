import json
import time
from django.http import HttpResponse
from django.contrib.auth.models import User

from product.models import Product
from checkout.models import Order, OrderItem, ShippingDetails


class StripeWHHandler:
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
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handler for payment_intent.succeeded webhook
        """
        # Gather data from Stripe payment intent
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        order_num = intent.metadata.order_num
        save_defaults = intent.metadata.save_defaults
        shipping_details = intent.charges.data[0].shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)
        intent_user = intent.metadata.user
        order_user = User.objects.get(username=intent_user)

        # Clean up shipping details data from Stripe
        # to remove blank strings
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Assume order does not exist yet,
        # check for existing order with delay counter
        # Will check for the order 5 times,
        # delaying for one second each time
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(order_num=order_num)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # If order exists already, return 200 response to Stripe
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                | SUCCESS: Order exists in database.',
                status=200)
        # If order does not exist, proceed with creating new order
        else:
            order = None
            cart = intent.metadata.cart
            try:
                # Create new order in DB using form details passed from Stripe
                order = Order.objects.create(
                    user=order_user,
                )
                # Create shipping details model and save to order
                order_shipping_details = ShippingDetails.objects.get_or_create(
                    order_num=order.order_num,
                    full_name=intent.charges.data.name,
                    email=shipping_details.email,
                    phone=shipping_details.phone,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    city=shipping_details.address.city,
                    state=shipping_details.address.state,
                    zipcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                )[0]
                order.shipping_details = order_shipping_details
                order.save()
                # Loop through cart provided in metadata to add order items
                for sku, item_data in json.loads(cart).items():
                    product = Product.objects.get(sku=sku)
                    order_item = OrderItem(
                        related_order=order,
                        buyer=order_user,
                        item=product,
                        quantity=item_data,
                        ordered=True,
                    )
                    order_item.save()
            # If an error occurs, delete order if created
            # and return error message to Stripe
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received:\
                                    {event["type"]} | ERROR: {e}',
                                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} |\
             SUCCESS: Order created in webhook handler.',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handler for payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received:\
            {event["type"]} | ERROR: Payment failed.',
            status=200)
