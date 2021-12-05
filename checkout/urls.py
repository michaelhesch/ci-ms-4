from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
)

app_name = 'checkout'

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('order-history/<order_num>/', OrderHistoryView.as_view(), name='order_history'),
]
