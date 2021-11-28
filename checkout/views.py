from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import View

from .models import Product, Order, OrderItem


# Order summary (cart detail) class based view
class OrderSummary(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order.")
            return redirect("/")


# Add items to the cart
@login_required
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
            messages.info(request, "Item quantity has been updated.")
            return redirect("checkout:cart")
        else:
            order.items.add(order_item)
            messages.info(request, "This item has been added to your cart.")
            return redirect("checkout:cart")
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date=order_date)
        order.items.add(order_item)
        messages.info(request, "This item has been added to your cart.")
        return redirect("checkout:cart")


# Remove item from the cart entirely, regardless of quantity
@login_required
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
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item has been removed from your cart.")
            return redirect("checkout:cart")
        else:
            messages.info(request, "This item is not in your cart.")
            return redirect("product:product_detail", slug=slug)
    else:
        messages.info(request, "You do not have any active orders.")
        return redirect("products:product_detail", slug=slug)


# Remove items from the cart by increment of 1
@login_required
def remove_one_from_cart(request, slug):
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
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("checkout:cart")
        else:
            messages.info(request, "This item is not in your cart.")
            return redirect("product:product_detail", slug=slug)
    else:
        messages.info(request, "You do not have any active orders.")
        return redirect("products:product_detail", slug=slug)
