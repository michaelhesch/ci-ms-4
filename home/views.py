from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product

class HomeView(ListView):
    model = Product
    paginate_by = 6
    template_name='index.html'


class StoreView(ListView):
    model = Product
    paginate_by = 6
    template_name='store.html'
