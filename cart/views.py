from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views.generic import View



# Order summary (cart detail) class based view
class ViewCart(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, 'cart.html')


# Add items to the cart
@login_required
def add_to_cart(request, sku):

    cart = request.session.get('cart', {})

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        if sku in list(cart.keys()):
            cart[sku] += quantity
        else:
            cart[sku] = quantity

        request.session['cart'] = cart
        messages.success(request, "Cart updated successfully!")
        return redirect(redirect_url)
    else:
        quantity = int(cart.get(sku))

        if sku in list(cart.keys()):
            cart[sku] += 1
        else:
            cart[sku] = quantity
        request.session['cart'] = cart
        messages.success(request, "Cart updated successfully!")
        return redirect('cart:cart')


# Remove item from the cart entirely, regardless of quantity
@login_required
def remove_from_cart(request, sku):
    cart = request.session.get('cart', {})
    quantity = cart.get(sku)

    if quantity > 0:
        cart.pop(sku)
        request.session['cart'] = cart
    else:
        messages.error(request, "Item has already been removed.")
        pass

    messages.success(request, "Item has been removed from your cart!")
    return redirect(reverse("cart:cart"))


# Remove items from the cart by increment of 1
@login_required
def remove_one_from_cart(request, sku):
    cart = request.session.get('cart', {})
    quantity = cart.get(sku)

    if sku in list(cart.keys()) and quantity > 1:
        cart[sku] -= 1
        request.session['cart'] = cart
        messages.success(request, "Cart updated successfully!")
        return redirect(reverse("cart:cart"))
    else:
        cart.pop(sku)
        request.session['cart'] = cart
        messages.success(request, "Item has been removed from your cart!")
        return redirect(reverse("cart:cart"))
