from django.shortcuts import render

# Create your views here.
#from .forms import ProductFrom
from .models import ProductDetails

def Home_view(request):
    product_home_list_obj   = ProductDetails.objects.all()
    product_home_list_count = ProductDetails.objects.all().count()
    context = {
        'product_home_list_obj'     : product_home_list_obj,
        'product_home_list_count'   : product_home_list_count,
    }
    return render(request, "home/home.html", context)
