from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Vat_rate

def cart_contents(request):

    cart_items = []
    line_total = 0
    line_vat = 0
    product_count = 0
    vat_rate = 0
    cart = request.session.get('cart', {})

    for item_id, qty in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        vat_rate = Vat_rate.objects.get(id=product.def_vat_rate.id)
        line_total += qty * product.sell_price
        line_vat += line_total * (vat_rate.rate/100)
        product_count += qty
        cart_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
        })

    # will be adding vat to this 
    grand_total = line_total + line_vat
    
    context = {
        'cart_items': cart_items,
        'net_total': line_total,
        'vat_total': line_vat,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
