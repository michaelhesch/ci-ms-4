from django import forms

from .models import Category, Product, ProductName, Review


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'category',
            'brand',
            'product_name',
            'description',
            'boost_clock',
            'memory_clock',
            'memory_size',
            'memory_type',
            'interface_type',
            'price',
            'image',
            'image_url',
        ]

    

    image = forms.ImageField(label='Image', required=False)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        product_names = ProductName.objects.all()


class ProductReview(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            'title',
            'body_content',
            'rating',
        ]
