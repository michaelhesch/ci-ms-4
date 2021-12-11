from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile, VendorProfile
from checkout.models import Order


class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        orders = Order.objects.filter(user=self.request.user, ordered=True)

        paginator = Paginator(orders, 6)
        context = {
            'username': profile.user,
            'verified': profile.verified,
            'avatar': profile.avatar_url,
            'orders': orders,
            'profile': profile,
            'page_obj': paginator,
        }

        return render(self.request, "profile.html", context)


class VendorProfileView(LoginRequiredMixin, ListView):
    model = VendorProfile
    paginate_by = 6
    template_name='store.html'


class OrderHistoryView(LoginRequiredMixin, ListView):
    template_name = 'order-history.html'
    ordering = '-order_date'
    paginate_by = 6

    def get_queryset(self):
        orders = Order.objects.get(user=self.request.user, ordered=True)
        self.queryset = orders.all()
        return super().get_queryset()
