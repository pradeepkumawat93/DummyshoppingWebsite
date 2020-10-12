from django import forms
from .models import Product

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'subcategory_1',
            'subcategory_2',
            'title',
            'description',
            'price',
            'image'
        ]