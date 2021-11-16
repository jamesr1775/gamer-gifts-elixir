from django.shortcuts import render
from django.conf import settings
from .models import Product

def all_products(request):
    """ View to return the products page """
    products = Product.objects.all()
    context = {
        'products': products,
        'star_loop': range(1, 6),
    }
    return render(request, 'products/products.html', context)
