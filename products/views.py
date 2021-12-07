from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

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
    profile = UserProfile.objects.get(user=request.user)
    others_bought_ids = []
    if product.products_others_bought:
        others_bought_ids = list(product.products_others_bought.split("_"))
    products_others_bought = []

    product_reviews = Review.objects.filter(product=product)
    orders = OrderLineItem.objects.filter(product=product, order__user_profile=profile)
    user_bought_product = True if orders else False
    if Review.objects.filter(product=product, user_profile=profile):
        users_submitted_review = Review.objects.filter(product=product, user_profile=profile)[0]
    else:
        users_submitted_review = []

    print(users_submitted_review)
    for pid in others_bought_ids:
        products_others_bought.append(get_object_or_404(Product, pk=pid))
    
    context = {
        'product': product,
        'star_loop': range(1, 6),
        'product_quantity_loop': range(1, 21),
        'products_others_bought': products_others_bought,
        'product_reviews': product_reviews,
        'user_bought_product': user_bought_product,
        'users_submitted_review': users_submitted_review,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ View to add product """
    if not request.user.is_superuser:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Make sure the form is valid.')

    template = 'products/add_product.html'
    context = {
        "form": form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ View to edit product """
    if not request.user.is_superuser:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))
    
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully edited product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Make sure the form is valid.')
    else:
        form = ProductForm(instance=product)
        
    template = 'products/edit_product.html'    
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ View to delete product """
    template = 'products/delete_product.html'
    if not request.user.is_superuser:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    if request.method == 'POST':
        messages.success(request, 'Successfully deleted product!')
        product.delete()
        return redirect(reverse('products'))
    return render(request, template, context)


@login_required
def add_product_review(request, product_id):
    """ View to add product review """
    template = 'products/product_review.html'
    if not request.user.is_authenticated:
        messages.error(request, "Error, you need to be logged in to leave a review.")
        return redirect(reverse('products'))
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        profile = UserProfile.objects.get(user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user_profile = profile
            review = form.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product review. Make sure the form is valid.')
    context = {
        "product": product,
        "form": form,
    }
    return render(request, template, context)

@login_required
def edit_product_review(request, review_id):
    """ View to edit product review """
    if not request.user.is_authenticated:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))
    review = get_object_or_404(Review, pk=review_id)
    print(review.rating)
    product = review.product
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully edited your review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update your review. Make sure the form is valid.')
    else:
        review.rating = float(review.rating)
        form = ReviewForm(instance=review)

    template = 'products/edit_product_review.html'
    context = {
        "form": form,
        'product': product,
        "review": review,
    }

    return render(request, template, context)


@login_required
def delete_product_review(request, review_id):
    """ View to delete product review """
    template = 'products/delete_product_review.html'
    if not request.user.is_authenticated:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))

    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    profile = UserProfile.objects.get(user=request.user)
    if Review.objects.filter(product=product, user_profile=profile):
        users_submitted_review = Review.objects.filter(product=product, user_profile=profile)[0]
    else:
        users_submitted_review = []
    context = {
        "product": product,
        "users_submitted_review": users_submitted_review,
        'star_loop': range(1, 6),
    }
    if request.method == 'POST':
        messages.success(request, 'Successfully deleted review!')
        review.delete()
        return redirect(reverse('product_detail', args=[product.id]))
    return render(request, template, context)
    

