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
    others_bought_ids = list(product.products_others_bought.split("_"))
    products_others_bought = []

    for pid in others_bought_ids:
        products_others_bought.append(get_object_or_404(Product, pk=pid))
    context = {
        'product': product,
        'star_loop': range(1, 6),
        'product_quantity_loop': range(1, 21),
        'products_others_bought': products_others_bought,
    }

    return render(request, 'products/product_details.html', context)