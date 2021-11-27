from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from .models import Category, Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
