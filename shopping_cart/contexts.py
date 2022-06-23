from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, qty in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += qty * product.sell_price
        product_count += qty
        cart_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
        })

    # will be adding vat to this 
    grand_total = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
