from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_shopping_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_product_to_bag(request, product_id):
    """ View to add product """
    product = get_object_or_404(Product, pk=product_id)
    product_quantity = int(request.POST.get('product_quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag = request.session.get('shopping_bag', {})

    if product_id in list(shopping_bag.keys()):
        shopping_bag[product_id] += product_quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_bag[product_id]}')
    else:
        shopping_bag[product_id] = product_quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)
