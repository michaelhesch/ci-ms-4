from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date_added',
        'product_name',
        'category',
        'seller',
        'price',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
