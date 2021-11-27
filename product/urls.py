from django.urls import path

from .views import (
    ProductDetail,
)

app_name = 'product'

urlpatterns = [
    path('<slug>/', ProductDetail.as_view(), name='product_detail'),
]
