from django.urls import path

from .views import (
    add_to_cart,
    remove_from_cart,
    remove_one_from_cart,
    ViewCart,
    CheckoutView,
    OrderHistoryView,
)

app_name = 'checkout'

urlpatterns = [
    path('add/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove-one/<slug>/', remove_one_from_cart, name='remove_one_from_cart'),
    path('cart/', ViewCart.as_view(), name='cart'),
    path('', CheckoutView.as_view(), name='checkout'),
    path('order-history/<order_num>/', OrderHistoryView.as_view(), name='order_history'),
]
