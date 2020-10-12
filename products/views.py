from django.shortcuts import render
# Create your views here.

from .forms import ProductFrom

def product_create_view(request):
    #form = ProductFrom(request.GET or None)
    #if form.is_valid():
    #    form.save()
    #    form = ProductFrom()

    #context = {
    #    "form" : form
    #}
    context = {}
    #return render(request, "home/home.html", context)#"product/product_create.html", context)
    return render(request, "home/home.html", context)