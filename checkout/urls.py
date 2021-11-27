from django.urls import path
from .views import (
    add_to_cart,
)

app_name = 'checkout'

urlpatterns = [
    path('add/<slug>/', add_to_cart, name='add_to_cart'),
]
