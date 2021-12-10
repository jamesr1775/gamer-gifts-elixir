from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from profiles.models import UserProfile
from .models import WishList


def wishlist(request):
    """ View to return the users Wishlist page """
    profile = UserProfile.objects.get(user=request.user)
    users_wishlist = WishList.objects.filter(user_profile=profile)
    products = []
    for item in users_wishlist:
        products.append(item.product)

    context = {
        'products': products,
        'star_loop': range(1, 6),
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_product_to_wishlist(request, product_id):
    """ View to add to users wishlist """
    profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    WishList.objects.get_or_create(
        user_profile=profile, product=product)
    return redirect(reverse('product_detail', args=[product.id]))


def remove_product_from_wishlist(request, product_id):
    """ View to remove product from users wishlist """
    profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist = WishList.objects.get(product=product, user_profile=profile)
    wishlist.delete()
    return redirect(reverse('wishlist'))
