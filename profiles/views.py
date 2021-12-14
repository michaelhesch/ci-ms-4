from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile, VendorProfile
from .forms import VendorRegistrationForm
from checkout.models import Order, OrderItem
from product.models import Product


class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        vendor_profile = VendorProfile.objects.get(user=self.request.user)
        orders = Order.objects.filter(user=self.request.user, ordered=True)
        unpaid_orders = OrderItem.objects.filter(vendor=vendor_profile, ordered=True, vendor_paid=False)
        paid_orders = OrderItem.objects.filter(vendor=vendor_profile, ordered=True, vendor_paid=True)

        unpaid_balance = 0
        for order in unpaid_orders:
            unpaid_balance += order.vendor_amount

        paid_balance = 0
        for order in paid_orders:
            paid_balance += order.vendor_amount

        #if orders.count() > 6:
        paginator = Paginator(orders, 6)

        context = {
            'username': profile.user,
            'verified': profile.verified,
            'avatar': profile.avatar_url,
            'orders': orders,
            'profile': profile,
            'vendor': vendor_profile,
            'unpaid_balance': unpaid_balance,
            'paid_balance': paid_balance,
            'page_obj': paginator,
        }

        return render(self.request, "profile.html", context)


class VendorStoreView(LoginRequiredMixin, View):
    model = VendorProfile
    template_name='vendor_store.html'

    def get(self, *args, **kwargs):
        store_slug = self.kwargs['store_slug']
        users_store = VendorProfile.objects.get(store_slug=store_slug)
        products = Product.objects.filter(seller=users_store.user_id)
        unpaid_orders = OrderItem.objects.filter(vendor=users_store, ordered=True, vendor_paid=False)
        paid_orders = OrderItem.objects.filter(vendor=users_store, ordered=True, vendor_paid=True)

        unpaid_balance = 0
        for order in unpaid_orders:
            unpaid_balance += order.vendor_amount

        paid_balance = 0
        for order in paid_orders:
            paid_balance += order.vendor_amount

        form_init = model_to_dict(users_store)
        form = VendorRegistrationForm(initial=form_init)

        context = {
            'form': form,
            'products': products,
            'store': users_store,
            'unpaid_balance': unpaid_balance,
            'paid_balance': paid_balance,
            'store_slug': users_store.store_slug,
        }
        return render(self.request, "vendor_store.html", context)

    def post(self, *args, **kwargs):

        form = VendorRegistrationForm(self.request.POST or None)
        store_slug = self.kwargs['store_slug']
        users_store = VendorProfile.objects.get(user=self.request.user)
        products = Product.objects.filter(seller=users_store.user_id)
        unpaid_orders = OrderItem.objects.filter(vendor=users_store, ordered=True, vendor_paid=False)
        paid_orders = OrderItem.objects.filter(vendor=users_store, ordered=True, vendor_paid=True)

        unpaid_balance = 0
        for order in unpaid_orders:
            unpaid_balance += order.vendor_amount

        paid_balance = 0
        for order in paid_orders:
            paid_balance += order.vendor_amount

        try:
            if self.request.user == users_store.user:
                # If order form is valid, update store name
                if form.is_valid():
                    if users_store.store_name == self.request.POST['store_name']:
                        pass
                    else:
                        store_name = self.request.POST['store_name']
                        users_store.store_name = store_name
                        users_store.save()
        except Exception as e:
            messages.error(self.request, f"An unexpected error occured: {e}.")

        # Update user_store object with latest profile
        users_store = VendorProfile.objects.get(user=self.request.user)        
        # Re-initialize form with updated value
        form_init = model_to_dict(users_store)
        form = VendorRegistrationForm(initial=form_init)
        # Re-check slug if updated so context is updated
        store_slug = users_store.store_slug

        context = {
            'form': form,
            'store': users_store,
            'products': products,
            'unpaid_balance': unpaid_balance,
            'paid_balance': paid_balance,
            'store_slug': store_slug,
        }

        return render(self.request, "vendor_store.html", context)

class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'order-history.html'
    ordering = '-order_date'
    paginate_by = 6

    def get_queryset(self):
        orders = Order.objects.get(user=self.request.user, ordered=True)
        self.queryset = orders.all()
        return super().get_queryset()
