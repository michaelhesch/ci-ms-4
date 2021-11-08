from django.contrib import admin
from .models import Category, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'category',
        'seller',
        'price',
        'date_added',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'added_by',
        'rating',
        'product_reviewed',
        'added_on',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
