from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


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


class EditProduct(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        seller = VendorProfile.objects.get(user=self.request.user)
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug, seller=seller)

        form_init = model_to_dict(product)
        form = ProductForm(initial=form_init)
        context = {
            'slug': slug,
            'form': form,
        }

        return render(self.request, 'edit_product.html', context)
    
    def post(self, *args, **kwargs):
        slug = self.kwargs['slug']
        seller_userprofile = VendorProfile.objects.get(user=self.request.user)
        store_slug = seller_userprofile.vendorprofile.store_slug
        existing_data = Product.objects.get(slug=slug, seller=seller_userprofile)

        if self.request.method == 'POST':
            try:
                form = ProductForm(self.request.POST, self.request.FILES)
                if form.is_valid():
                    category = form.cleaned_data.get('category')
                    product_name = form.cleaned_data.get('product_name')
                    description = form.cleaned_data.get('description')
                    brand = form.cleaned_data.get('brand')
                    boost_clock = form.cleaned_data.get('boost_clock')
                    memory_clock = form.cleaned_data.get('memory_clock')
                    memory_type = form.cleaned_data.get('memory_type')
                    interface_type = form.cleaned_data.get('interface_type')
                    price = form.cleaned_data.get('price')

                    existing_data.category = category
                    existing_data.product_name = product_name
                    existing_data.description = description
                    existing_data.brand = brand
                    existing_data.boost_clock = boost_clock
                    existing_data.memory_clock = memory_clock
                    existing_data.memory_type = memory_type
                    existing_data.interface_type = interface_type
                    existing_data.price = price
                    existing_data.image_url = existing_data.image_url

                    existing_data.save()

                    messages.success(self.request, "Your product is updated!")
                    return redirect(reverse("profiles:vendorprofile", kwargs={'store_slug': store_slug}))
                else:
                    messages.warning(self.request, "Your product was not updated,\
                        please try again")
                    return redirect(reverse("profiles:vendorprofile", kwargs={'store_slug': store_slug}))
            except Exception as e:
                messages.error(self.request, f"An unexpected error occured: {e}")
                return redirect(reverse("profiles:vendorprofile", kwargs={'store_slug': store_slug}))


class ReviewProduct(LoginRequiredMixin, View):
    model = Review
    def get(self, *args, **kwargs):
        product = Product.objects.get(slug=self.kwargs['slug'])

        existing_review = Review.objects.filter(product_reviewed=product, added_by=self.request.user).exists()
        if existing_review:
            review = Review.objects.get(product_reviewed=product, added_by=self.request.user)
            form_init = model_to_dict(review)
            form = ProductReview(initial=form_init)
        else:
            form = ProductReview()

        context = {
            'form': form,
            'product': product,
        }
        return render(self.request, 'review_product.html', context)
    
    def post(self, *args, **kwargs):
        form = ProductReview(self.request.POST or None)
        product_slug = self.kwargs['slug']
        product = Product.objects.get(slug=product_slug)

        try:
            if form.is_valid():
                title = self.request.POST['title']
                body_content = self.request.POST['body_content']
                added_by = self.request.user
                rating = self.request.POST['rating']
                product_reviewed = product

                review = Review.objects.get_or_create(product_reviewed=product, added_by=added_by)[0]
                review.title = title
                review.body_content = body_content
                review.added_by = added_by
                review.rating = rating
                review.product_reviewed = product_reviewed
                review.save()

                return redirect(reverse("product:product_detail", kwargs={'slug': product_slug}))
        
        except Exception as e:
             messages.error(self.request, f"An unexpected error occured: {e}.")
             return redirect("product:product_detail", slug=product_slug)


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


@login_required
def delete_review(request, sku):
    product = Product.objects.get(sku=sku)
    product_slug = product.slug
    review = Review.objects.get(product_reviewed=product, added_by=request.user)

    try:
        if request.method == 'POST':
            review.delete()
            messages.success(request, "Your review has been deleted.")
            return redirect(reverse("product:product_detail", kwargs={'slug': product_slug}))
    except Exception as e:
        messages.error(request, f"An unexpected error occured: {e}")
        return redirect(reverse("product:product_detail", kwargs={'slug': product_slug}))
