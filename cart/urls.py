from django.urls import path

from cart.views import (
    add_to_cart,
    remove_from_cart,
    remove_one_from_cart,
    ViewCart,
)

app_name = 'cart'

urlpatterns = [
    path('add/<sku>/', add_to_cart, name='add_to_cart'),
    path('remove/<sku>/', remove_from_cart, name='remove_from_cart'),
    path('remove-one/<sku>/',
         remove_one_from_cart,
         name='remove_one_from_cart'),
    path('', ViewCart.as_view(), name='cart'),
]
