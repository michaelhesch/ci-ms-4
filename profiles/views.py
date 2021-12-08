from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile
from checkout.models import Order


class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        orders = Order.objects.filter(user=self.request.user, ordered=True)

        context = {
            'username': profile.user,
            'verified': profile.verified,
            'orders': orders,
            'avatar': profile.avatar_url,
        }

        return render(self.request, "profile.html", context)
