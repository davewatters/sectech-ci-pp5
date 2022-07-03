from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product


@login_required
def checkout(request):
    '''
    View that renders the checkout page.
    '''
    context = {}
    return render(request, 'checkout/checkout.html' )