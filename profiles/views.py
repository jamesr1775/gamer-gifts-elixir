from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ View to view user profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        else:
            messages.error(request, 'Failed to update Profile. Please make sure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


def get_order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)