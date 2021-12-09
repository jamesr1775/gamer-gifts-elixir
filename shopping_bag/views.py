from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from products.models import Product


def view_shopping_bag(request):
    """ A view that renders the bag contents page """
    context = {
        'product_quantity_loop': range(1, 21),
    }
    return render(request, 'shopping_bag/shopping_bag.html', context)


def add_product_to_bag(request, product_id):
    """ View to add product """
    product = get_object_or_404(Product, pk=product_id)
    product_quantity = int(request.POST.get('product_quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if product_id in shopping_bag.keys():
            if size in shopping_bag[product_id]['item_with_sizes'].keys():
                if shopping_bag[product_id][
                    'item_with_sizes'][size] + product_quantity > \
                        settings.MAX_ORDER_QUANTITY:
                    messages.error(
                        request, f'Failed to add {product.name} \
                            to your bag, Maximum quantity is \
                            {settings.MAX_ORDER_QUANTITY}')
                    request.session['shopping_bag'] = shopping_bag
                    return redirect(redirect_url)
                shopping_bag[product_id][
                    'item_with_sizes'][size] += product_quantity
            else:
                shopping_bag[product_id][
                    'item_with_sizes'][size] = product_quantity
        else:
            shopping_bag[product_id] = {
                'item_with_sizes': {size: product_quantity}}
            messages.success(
                request, f'Added size {size.upper()} {product.name} \
                    to your bag')
    else:
        if product_id in shopping_bag:
            shopping_bag[product_id] += product_quantity
            messages.success(
                request, f'Updated {product.name} quantity to \
                    {shopping_bag[product_id]}')
        else:
            shopping_bag[product_id] = product_quantity
            messages.success(request, f'Added {product.name} to your bag')
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    """ View to update basket """
    product_quantity = int(request.POST.get('product_quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        shopping_bag[product_id]['item_with_sizes'][size] = product_quantity
    else:
        shopping_bag[product_id] = product_quantity
    request.session['shopping_bag'] = shopping_bag
    context = {
        'product_quantity_loop': range(1, 21),
    }
    return render(request, 'shopping_bag/shopping_bag.html', context)


def remove_product_from_bag(request, product_id):
    """ View to add product """
    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None
        shopping_bag = request.session.get('shopping_bag', {})
        if isinstance(shopping_bag[product_id], dict):
            size = request.GET.get('product_size')
            del shopping_bag[product_id]['item_with_sizes'][size]
            if not shopping_bag[product_id]['item_with_sizes']:
                shopping_bag.pop(product_id)
            messages.success(
                request, f'Removed size {size.upper()} {product.name} \
                    from your bag')
        else:
            shopping_bag.pop(product_id)
            messages.success(request, f'Removed {product.name} from your bag')
        request.session['shopping_bag'] = shopping_bag
        context = {
            'product_quantity_loop': range(1, 21),
        }
        return render(request, 'shopping_bag/shopping_bag.html', context)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
