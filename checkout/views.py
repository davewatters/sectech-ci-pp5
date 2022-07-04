from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from customers.models import Customer
from customers.forms import CustomerForm
from shopping_cart.contexts import cart_contents


@login_required
def checkout(request):
    '''
    View that renders the checkout page.
    '''
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':
        pass
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your shopping cart is empty.")
            return redirect(reverse('products'))

    context = {
        'customer': customer,
    }

    return render(request, 'checkout/checkout.html', context )