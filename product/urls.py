from django.urls import path

from .views import (
    ProductDetail,
    ListProduct,
)

app_name = 'product'

urlpatterns = [
    path('add/', ListProduct.as_view(), name='add'),
    path('<slug>/', ProductDetail.as_view(), name='product_detail'),
]
