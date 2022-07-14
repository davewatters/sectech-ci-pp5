from django.shortcuts import get_object_or_404
from products.models import Product, Vat_rate


def cart_contents(request):
    '''
    Define a context processor function to make shopping cart items
    available in multiple templates.
    Related: sectech.settings.TEMLPATES
    '''
    cart_items = []
    vat_rate = 0
    line_cost = 0
    line_vat = 0
    cart_net_amt = 0
    cart_vat_amt = 0
    cart_total = 0
    cart = request.session.get('cart', {})
    for item_id, qty in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        vat_rate = Vat_rate.objects.get(id=product.def_vat_rate.id)
        line_cost = (qty * product.sell_price)
        line_vat = (line_cost * (vat_rate.rate/100))
        line_total = line_cost + line_vat
        cart_net_amt += line_cost
        cart_vat_amt += line_vat
        cart_total += line_total
        cart_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'net_total': cart_net_amt,
        'vat_total': cart_vat_amt,
        'grand_total': cart_total,
    }

    return context
