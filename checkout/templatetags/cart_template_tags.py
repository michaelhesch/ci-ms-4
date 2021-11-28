from django import template
from checkout.models import Order


register = template.Library()


@register.filter
def cart_counter(user):
    if user.is_authenticated:
        # Check for order by current user that is not complete
        queryset = Order.objects.filter(user=user, ordered=False)
        if queryset.exists():
            return queryset[0].items.count()
        return 0
