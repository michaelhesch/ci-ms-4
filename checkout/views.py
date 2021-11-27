from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from .models import Product, Order, OrderItem


# Add items to the cart
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        buyer=request.user,
        ordered=False,
        )
    order_queryset = Order.objects.filter(user=request.user, ordered=False)
    # Check if an existing order is present for user
    if order_queryset.exists():
        # Select current order
        order = order_queryset[0]
        # Check if item is in the order already and increase quantity by 1
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("product:product_detail", slug=slug)
        else:
            order.items.add(order_item)
            return redirect("product:product_detail", slug=slug)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=order_date)
        order.items.add(order_item)

    return redirect("product:product_detail", slug=slug)


# Remove items from the cart
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_queryset = Order.objects.filter(
        user=request.user,
        ordered=False,
    )
    if order_queryset.exists():
        order = order_queryset[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                buyer=request.user,
                ordered=False,
            )
            order.items.remove(order_item)
            order_item.delete()
            return redirect("product:product_detail", slug=slug)
        else:
            return redirect("product:product_detail", slug=slug)
    else:
        return redirect("products:product_detail", slug=slug)
