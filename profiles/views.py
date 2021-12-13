from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile, VendorProfile
from checkout.models import Order
from product.models import Product


class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        vendor_profile = VendorProfile.objects.get(user=self.request.user)
        orders = Order.objects.filter(user=self.request.user, ordered=True)

        paginator = Paginator(orders, 6)
        context = {
            'username': profile.user,
            'verified': profile.verified,
            'avatar': profile.avatar_url,
            'orders': orders,
            'profile': profile,
            'vendor': vendor_profile,
            'page_obj': paginator,
        }

        return render(self.request, "profile.html", context)


class VendorProfileView(LoginRequiredMixin, View):
    model = VendorProfile
    template_name='vendor_store.html'

    def get(self, *args, **kwargs):
        store_slug = self.kwargs.get('store_slug')
        users_store = VendorProfile.objects.get(store_slug=store_slug)
        products = Product.objects.filter(seller=users_store.user_id)

        context = {
            'products': products,
            'store': users_store,
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
