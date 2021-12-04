from django.urls import path
from .views import (
    HomeView,
    StoreView,
)
from product.views import (
    ProductDetail,
)

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('store/', StoreView.as_view(), name='store'),
]
