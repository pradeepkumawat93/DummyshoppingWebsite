from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    category          =   models.CharField(max_length=50)
    subcategory_1     =   models.CharField(max_length=50)
    subcategory_2     =   models.CharField(max_length=50)
    title             =   models.CharField(max_length=50)
    description       =   models.TextField(blank=True, null=True)
    price             =   models.DecimalField(decimal_places=2, max_digits=100000)
    sale              =   models.BooleanField(blank=True, null=True)
    image             =   models.ImageField(blank=True)
