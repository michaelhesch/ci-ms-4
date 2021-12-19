from django import template

register = template.Library()


# Template tag to return subtotals for line items in cart
@register.filter
def cart_subtotal(price, quantity):
    return price * quantity
