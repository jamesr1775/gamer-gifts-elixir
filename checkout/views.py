from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm
import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    shopping_bag = request.session.get('shopping_bag', {})
    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'Test',
    }

    return render(request, template, context)