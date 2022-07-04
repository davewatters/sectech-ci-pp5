from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from customers.models import Customer
from customers.forms import CustomerForm


@login_required
def checkout(request):
    '''
    View that renders the checkout page.
    '''
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':
        pass
    else:
        pass
        
    context = {
        'customer': customer,
    }

    return render(request, 'checkout/checkout.html', context )