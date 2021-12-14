from django.urls import path

from .views import (
    ProductDetail,
    ListProduct,
    ReviewProduct,
    remove_item_from_store,
)

app_name = 'product'

urlpatterns = [
    path('add/', ListProduct.as_view(), name='add'),
    path('<slug>/', ProductDetail.as_view(), name='product_detail'),
    path('remove-item/<sku>/', remove_item_from_store, name='remove_item'),
    path('review/<slug>/', ReviewProduct.as_view(), name='product_review'),
]
