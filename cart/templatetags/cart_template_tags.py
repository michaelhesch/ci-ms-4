from django import template
from checkout.models import Order


register = template.Library()


# Template tag to return subtotals for line items in cart
@register.filter
def cart_subtotal(price, quantity):
    return price * quantity
