from django import forms
from .models import Product

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'image',
        ]