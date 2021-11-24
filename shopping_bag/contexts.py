from django.conf import settings 
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def shopping_bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('shopping_bag', {})

    for product_id, product_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        if isinstance(product_data, dict):
            for size, quantity in product_data['item_with_sizes'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
        else:
            total += product_data * product.price
            product_count += product_data
            bag_items.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context