from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile
from checkout.models import OrderLineItem


def all_products(request):
    """ View to return the products page """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # if sort or search
    if request.GET:
        # getting sort direction
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

        # get products of category type
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        # get products of gender type
        if 'gender' in request.GET:
            gender = [request.GET['gender'], 'both']
            products = products.filter(product_type__in=gender)
        # if user searched get search query and find products
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
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
    products_others_bought = []
    users_submitted_review = []
    user_bought_product = False

    # create products others bought id list
    if product.products_others_bought:
        others_bought_ids = list(product.products_others_bought.split("_"))
    product_reviews = Review.objects.filter(product=product)

    # get the users review if they made one
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        orders = OrderLineItem.objects.filter(
            product=product, order__user_profile=profile)
        user_bought_product = True if orders else False
        if Review.objects.filter(product=product, user_profile=profile):
            users_submitted_review = Review.objects.filter(
                product=product, user_profile=profile)[0]

    # create products others bought list
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

    # Check add product form and add if valid
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Make sure the form is valid.')

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

    # Check edit product form and update if valid
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully edited product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Make sure the form is valid.')
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
    # Check confirm delete pressed so delete the product
    if request.method == 'POST':
        messages.success(request, 'Successfully deleted product!')
        product.delete()
        return redirect(reverse('products'))
    return render(request, template, context)


@login_required
def add_product_review(request, product_id):
    """ View to add product review """
    profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    orders = OrderLineItem.objects.filter(
        product=product, order__user_profile=profile)
    user_bought_product = True if orders else False
    template = 'products/product_review.html'

    # Make sure user is logged in and also has purchased the product
    if not request.user.is_authenticated or not user_bought_product:
        messages.error(
            request,
            "Error, you need to be logged in and have purchased the \
                product to leave a review.")
        return redirect(reverse('products'))

    # save the review and update product rating in product model
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user_profile = profile
            review = form.save()
            product.product_rating = product.getAverageRating()
            product.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product review. Make sure the form is valid.')
    context = {
        "product": product,
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_product_review(request, review_id):
    """ View to edit product review """
    review = get_object_or_404(Review, pk=review_id)
    profile = UserProfile.objects.get(user=request.user)
    product = review.product
    user_reviewed_product = True if review.user_profile == profile else False

    # Make sure user is logged in and also has purchased the product
    if not request.user.is_authenticated or not user_reviewed_product:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))

    # Update review if form is valid
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            product.product_rating = product.getAverageRating()
            product.save()
            messages.success(request, 'Successfully edited your review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update your review. Make sure the form is valid.')
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
    review = get_object_or_404(Review, pk=review_id)
    profile = UserProfile.objects.get(user=request.user)
    product = review.product
    user_reviewed_product = True if review.user_profile == profile else False
    # Make sure user is logged in and also has purchased the product
    if not request.user.is_authenticated or not user_reviewed_product:
        messages.error(request, "Error, you do not have permission.")
        return redirect(reverse('products'))

    # Make sure user review exists
    if Review.objects.filter(product=product, user_profile=profile):
        users_submitted_review = Review.objects.filter(
            product=product, user_profile=profile)[0]
    else:
        users_submitted_review = []

    # delete review if confirm delete button posted
    if request.method == 'POST':
        messages.success(request, 'Successfully deleted review!')
        review.delete()
        product.product_rating = product.getAverageRating()
        product.save()
        return redirect(reverse('product_detail', args=[product.id]))
    template = 'products/delete_product_review.html'
    context = {
        "product": product,
        "users_submitted_review": users_submitted_review,
        'star_loop': range(1, 6),
    }
    return render(request, template, context)


def get_latest_products(request):
    """ View to return most recent added products """
    products = Product.objects.order_by("-id")
    latest_products = products[:20]
    latest_products_dict = {product.id: product for product in latest_products}
    print(latest_products_dict)
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

    filtered_products = []
    for product in products:
        if product.id in latest_products_dict:
            filtered_products.append(product)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': filtered_products,
        'star_loop': range(1, 6),
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def get_popular_products(request):
    """ View to return the highest reviewed products """
    products = Product.objects.order_by("-product_rating")
    popular_products = products[:20]
    popular_products_dict = {
        product.id: product for product in popular_products}
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
    current_sorting = f'{sort}_{direction}'

    filtered_products = []
    for product in products:
        if product.id in popular_products_dict:
            filtered_products.append(product)

    context = {
        'products': filtered_products,
        'star_loop': range(1, 6),
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)
