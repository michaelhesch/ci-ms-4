from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from product.forms import ProductForm

from .models import Product, Review
from .forms import ProductReview
from profiles.models import UserProfile, VendorProfile


class ProductDetail(LoginRequiredMixin, View):
    model = Product
    template_name = 'product_detail.html'

    def get(self, *args, **kwargs):
        slug = self.kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        reviews = Review.objects.filter(product_reviewed=product)

        context = {
            'product': product,
            'reviews': reviews,
        }
        return render(self.request, 'product_detail.html', context)


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


class ReviewProduct(LoginRequiredMixin, View):
    model = Review
    def get(self, *args, **kwargs):
        form = ProductReview()
        product = Product.objects.get(slug=self.kwargs['slug'])

        context = {
            'form': form,
            'product': product,
        }
        return render(self.request, 'review_product.html', context)
    
    def post(self, *args, **kwargs):

        return


# Delete product from the store
@login_required
def remove_item_from_store(request, sku):
    if request.method == 'POST':
        try:
            product = Product.objects.get(sku=sku)
            vendor = VendorProfile.objects.get(user=request.user)
            store_slug = vendor.store_slug

            if request.user == product.seller.user:
                product.delete()
                messages.success(request, "Your product has been removed.")
                return redirect('profiles:vendorprofile', store_slug=store_slug)
            else:
                messages.error(request, "You can only manage your own products.")
                pass

        except Exception as e:
            messages.error(request, f"Error (500): {e}")
            return HttpResponse(status=500)
