import random
from datetime import datetime
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from profiles.models import UserProfile


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category_order']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name


class ProductName(models.Model):
    product_name = models.CharField(max_length=200, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Product Names'
    
    def __str__(self):
        return self.product_name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sku = models.CharField(max_length=20, null=False, editable=False)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductName, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=120)
    boost_clock = models.CharField(max_length=15)
    memory_clock = models.CharField(max_length=15)
    memory_size = models.CharField(max_length=20)
    memory_type = models.CharField(max_length=10)
    interface_type = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="product/", null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="product/thumbnails/", null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Products'
    
    # Over-ride default save function to set slug field
    def save(self, *args, **kwargs):
        self.sku = random.randrange(10**1, 10**20)
        slug_name = str(self.seller) + str(self.product_name.product_name)
        self.slug = slugify(slug_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name.product_name

    # Helper function to create list of suggested similar products
    def get_similar_products(self):
        similar_products = list(self.category.products.exclude(sku=self.sku))
        if len(similar_products) >= 4:
            similar_products = random.sample(similar_products, 4)

        return similar_products
        

    # Placeholder for function to get thumbnail, or make thumbnail from uploaded image


    # Placeholder for make thumbnail helper function


    # Helper function to determine if a 'New' tag should be added to items in the store
    def determine_if_new(self):
        now = datetime.now().date()
        added_date = self.date_added.date()
        delta = now - added_date
        
        if delta.days > 7:
            return False
        else:
            return True

    # Helper function to return category to UI
    def get_category_display(self):
        return self.category.category_name

    # Generate url for products to be used in front-end navigation
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={
            'slug': self.slug,
            })

    # Add product to cart url helper function
    def get_add_to_cart_url(self):
        return reverse("cart:add_to_cart", kwargs={
            'slug': self.slug,
            })

    # Remove product from cart url helper function
    def get_remove_from_cart_url(self):
        return reverse("cart:remove_from_cart", kwargs={
            'slug': self.slug,
            })

    # Helper function to calculate the item's selling fee
    def get_selling_fee(self):
        selling_fee = round(self.price * round(Decimal(settings.SELLING_FEE_PERCENTAGE / 100), 2), 2)
        return selling_fee

class Review(models.Model):
    title = models.CharField(max_length=100)
    body_content = models.TextField()
    added_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    product_reviewed = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.title
