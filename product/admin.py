from django.contrib import admin
from .models import Category, ProductName, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'sku',
        'category',
        'seller',
        'price',
        'date_added',
    )


class ProductNameAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'category',
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
admin.site.register(ProductName, ProductNameAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
