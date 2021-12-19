from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
    cache_checkout_data,
)
from .webhooks import (
    webhook
)

app_name = 'checkout'

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('order-history/<order_num>/',
         OrderHistoryView.as_view(), name='order_history'),
    path('cache_checkout_data/',
         cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook')
]
