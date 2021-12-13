from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from product.forms import ProductForm

from .models import Category, Product
from profiles.models import UserProfile


class ProductDetail(LoginRequiredMixin, View):
    model = Product
    template_name = 'product_detail.html'

    def get(self, *args, **kwargs):
        slug = self.kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context = {
            'product': product,
        }
        return render(self.request, 'product/product_detail.html', context)

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
                seller_userprofile = UserProfile.objects.get(user=self.request.user)
                product.seller = seller_userprofile
                form.save()

                context = {
                    'slug': product.slug,
                }
                messages.success(self.request, "Your product has been added successfully.")
                return redirect(reverse('product:product_detail', args=[product.slug]))
            else:
                messages.error(self.request, "Failed to add product, please try again.")
        else:
            form = ProductForm()

        context = {
            'form': form,
        }

        return render(self.request, 'add_product.html', context)
