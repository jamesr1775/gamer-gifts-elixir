from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):
    """ View to show a products details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        'star_loop': range(1, 6),
        'product_quantity_loop': range(1, 21),
    }

    return render(request, 'products/product_details.html', context)