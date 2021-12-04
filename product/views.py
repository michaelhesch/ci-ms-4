from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from product.forms import ProductForm

from .models import Category, Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ListProduct(LoginRequiredMixin, View):
    model = Product
    template_name = 'add_product.html'

    def get(self, *args, **kwargs):
        form = ProductForm()
        context = {
            'form': form,
        }

        return render(self.request, 'add_product.html', context)
    
    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            form = ProductForm(self.request.POST, self.request.FILES)

            if form.is_valid():
                product = form.save(commit=False)
                product.seller = self.request.user
                form.save()

                context = {
                    'slug': product.slug,
                }
                messages.success(self.request, "Your product has been added successfully.")
                return render(self.request, 'product_detail.html', context)
            else:
                messages.error(self.request, "Failed to add product, please try again.")
        else:
            form = ProductForm()

        context = {
            'form': form,
        }

        return render(self.request, 'add_product.html', context)
