from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import View

from .forms import CheckoutForm
from .models import Order, OrderItem, BillingAddress
from profiles.models import UserProfile


# Render checkout form and handle checkout form submit
class CheckoutView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.warning(self.request, "There is nothing in your cart.")
            return redirect("home:store")
        
        form = CheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.warning(self.request, "There is nothing in your cart.")
            return redirect("home:store")
        
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Order.objects.get_or_create(user=self.request.user, ordered=False)[0]
            billing_address = BillingAddress.objects.get_or_create(user=self.request.user)[0]

            if form.is_valid():
                address1 = form.cleaned_data.get('address1')
                address2 = form.cleaned_data.get('address2')
                state = form.cleaned_data.get('state')
                city = form.cleaned_data.get('city')
                zipcode = form.cleaned_data.get('zipcode')
                country = form.cleaned_data.get('country')
                # TODO: add these for checkbox fields in form 
                # billing_same = form.cleaned_data.get('billing_same')
                save_defaults = form.cleaned_data.get('save_defaults')
                billing_address.user = self.request.user
                billing_address.address1=address1
                billing_address.address2=address2
                billing_address.state=state
                billing_address.city=city
                billing_address.zipcode=zipcode
                billing_address.country=country
                billing_address.save()
                order.billing_address=billing_address
                order.save()

                # Update profile defaults if option selected
                if save_defaults == True:
                    profile = UserProfile.objects.get(user=self.request.user)
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
                """
                # Select order items related to current order
                items = OrderItem.objects.filter(buyer=self.request.user, ordered=False)
                # Set ordered status and order number for order items
                for item in items:
                    item.related_order = order.order_num
                    item.ordered = True
                    item.save()
                # Set order date and overall order ordered status to True and save
                order.order_date = timezone.now()
                order.ordered = True
                order.save()
                """
                # Clean out session cart
                self.request.session.pop('cart')

                context = {
                    'order': order,
                    #'items': order.items.all,
                }
                messages.success(self.request, "Thank you, your order has been placed!")
                return render(self.request, 'checkout_success.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order.")
            return redirect("cart:cart")


class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request, order_num):
        order = get_object_or_404(Order, order_num=order_num)

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'order_history': True,
        }

        return render(request, template, context)
