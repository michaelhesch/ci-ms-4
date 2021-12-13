from django.urls import path
from .views import (
    HomeView,
    products_store,
)


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('store/', products_store, name='store'),
]
