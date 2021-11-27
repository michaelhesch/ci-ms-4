from django.urls import path
from .views import (
    HomeView,
)
from product.views import (
    ProductDetail,
)

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
