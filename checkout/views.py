import stripe
import json

from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.utils import timezone
from django.views.generic import View

from .forms import CheckoutForm
from .models import Order, OrderItem, ShippingDetails
from product.models import Product
from profiles.models import UserProfile
from cart.contexts import cart_contents


@require_POST
def cache_checkout_data(request):
    try:
        # Retrieve payment intent ID from the post request
        pid = request.POST.get('client_secret').split('_secret')[0]
        order_num = request.POST.get('order_num')
        save_defaults = request.POST.get('save_defaults')
        cart = json.dumps(request.session.get('cart', {}))
        # Setup Stripe to modify the payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify payment intent with additional metadata fields not captured in intent
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': cart,
            'save_defaults': save_defaults,
            'order_num': order_num,
            'user': request.user,
        })
        print(request)
        print(request.POST.get('order_num'))
        
        # Return 200 to continue processing in checkout.js
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot \
            be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Render checkout form and handle checkout form submit
class CheckoutView(LoginRequiredMixin,View):

    def get(self, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        
        cart = self.request.session.get('cart', {})
        
        if cart:
            # Create blank order to get new order number if user has a cart
            # Set UserProfile for new order
            order = Order.objects.get_or_create(user=self.request.user, ordered=False)[0]
            user_profile = UserProfile.objects.get(user=self.request.user)
            order.user_profile = user_profile
            order.save()
        else:
            messages.warning(self.request, "There is nothing in your cart.")
            return redirect("home:store")
        
        current_cart = cart_contents(self.request)
        cart_total = current_cart.get('grand_total')
        stripe_total = round(cart_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        form = CheckoutForm()
        template = 'checkout/checkout.html'
        context = {
            'form': form,
            'order': order,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(self.request, template, context)

    def post(self, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.warning(self.request, "There is nothing in your cart.")
            return redirect("home:store")

        form_data = {
            'full_name': self.request.POST['full_name'],
            'email': self.request.POST['email'],
            'phone': self.request.POST['phone'],
            'address1': self.request.POST['address1'],
            'address2': self.request.POST['address2'],
            'city': self.request.POST['city'],
            'state': self.request.POST['state'],
            'zipcode': self.request.POST['zipcode'],
            'country': self.request.POST['country'],
            'email': self.request.POST['email'],
        }

        form = CheckoutForm(self.request.POST or None)

        try:
            # Retrieve current order or create new order if missing
            order = Order.objects.get_or_create(user=self.request.user, ordered=False)[0]

            # If order form is valid, proceed with checkout logic
            if form.is_valid():  
                full_name = form.cleaned_data.get('full_name')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')
                address1 = form.cleaned_data.get('address1')
                address2 = form.cleaned_data.get('address2')
                state = form.cleaned_data.get('state')
                city = form.cleaned_data.get('city')
                zipcode = form.cleaned_data.get('zipcode')
                country = form.cleaned_data.get('country')
                if form.data.get('save-defaults') == 'on':
                    save_defaults = True
                else:
                    save_defaults = False

                # Create shipping details object and save to order
                shipping_details = ShippingDetails.objects.create(
                    user=self.request.user,
                    order_num=order,
                    full_name=full_name,
                    email=email,
                    phone=phone,
                    address1=address1,
                    address2=address2,
                    state=state,
                    city=city,
                    zipcode=zipcode,
                    country=country,
                )
                shipping_details.save()
                order.shipping_details = shipping_details

                # Update profile defaults if option selected
                if save_defaults == True:
                    profile = UserProfile.objects.get(user=self.request.user)
                    profile.default_email = email
                    profile.default_phone = phone
                    profile.default_address1 = address1
                    if address2:
                        profile.default_address2 = address2
                    else:
                        profile.default_address2 = ""
                    profile.default_city = city
                    profile.default_state = state
                    profile.default_zipcode = zipcode
                    profile.default_country = country
                    profile.save()
                    order.user_profile = profile

                # Retrieve Stripe intent PID and save to order
                pid = self.request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                # Create order items for cart items, set attributes
                for sku, item_data in cart.items():
                        try:
                            product = Product.objects.get(sku=sku)
                            order_item = OrderItem(
                                related_order=order,
                                buyer=self.request.user,
                                item=product,
                                quantity=item_data,
                                ordered=True,
                            )
                            order_item.save()
                        except Product.DoesNotExist:
                            messages.error(self.request, (
                                "One of the products in your bag does not exist!")
                            )
                            order.delete()
                            return redirect('cart:cart')

                # Set order date and overall order ordered status to True and save
                current_cart = cart_contents(self.request)
                cart_total = current_cart.get('grand_total')
                order.grand_total = cart_total
                order.order_date = timezone.now()
                order.ordered = True
                order.save()

                # Clean out session cart after order finalized
                self.request.session.pop('cart')

                context = {
                    'order': order,
                }
                messages.success(self.request, "Thank you, your order has been placed!")
                return render(self.request, 'checkout_success.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order.")
            return redirect("cart:cart")


class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request, order_num):
        order = get_object_or_404(Order, order_num=order_num, ordered=True)

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'order_history': True,
        }

        return render(request, template, context)
