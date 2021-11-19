from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category


def all_products(request):
    """ View to return the products page """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'gender' in request.GET:
            gender = [request.GET['gender'], 'both']
            products = products.filter(product_type__in=gender)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'star_loop': range(1, 6),
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ View to show a products details """
    product = get_object_or_404(Product, pk=product_id)
    others_bought_ids = []
    if others_bought_ids:
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