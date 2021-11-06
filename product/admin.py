from django.contrib import admin
from .models import Category, Product


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
