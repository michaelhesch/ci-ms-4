from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category_order']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.product_name

    # Placeholder for function to get thumbnail, or make thumbnail from uploaded image


    # Placeholder for make thumbnail helper function


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
