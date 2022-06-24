from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product


def view_cart(request):
    '''
    View that renders the contents of the shopping cart.
    '''

    return render(request, 'shopping_cart/cart.html' )


def add_to_cart(request, item_id):
    '''
    Adds a product to the shopping cart or 
    increase its qty count if product already in cart.
    '''

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.desc} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.desc} to your cart')

    request.session['cart'] = cart

    return redirect('product-list')
