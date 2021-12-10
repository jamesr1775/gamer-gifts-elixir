from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from products.models import UserProfile
from .models import WishList

def wishlist(request):
    """ View to return the users Wishlist page """
    profile = UserProfile.objects.get(user=request.user)
    users_wishlist =  WishList.objects.filter(user_profile=profile)
    print(users_wishlist)

    products = []
    for item in users_wishlist:
        products.append(item.product)

    context = {
        'products': products,
    }
    return render(request, 'wishlist/wishlist.html', context)


def add_product_to_wishlist(request, product_id):
    """ View to add to users wishlist """
    profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = WishList.objects.get_or_create(user_profile=profile, product=product)
    users_wishlist = WishList.objects.filter(user_profile=profile)
    # Add product to the wishlist
    context = {
        'products': users_wishlist,
    }
    return redirect(reverse('wishlist'))
