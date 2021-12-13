from django.urls import path

from . import apps

from .views import (
    ProfileView,
    OrderHistoryView,
    VendorProfileView,
)

app_name = apps.ProfilesConfig.name

urlpatterns = [
    path('<username>/', ProfileView.as_view(), name='profile'),
    path('order-history/', OrderHistoryView.as_view(), name='orderhistory'),
    path('vendor/<store_slug>/', VendorProfileView.as_view(), name='vendorprofile'),
]
