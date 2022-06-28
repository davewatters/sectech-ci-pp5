from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from .models import Customer


def customer_detail(request):
    '''
    View shows detail of logged-in customer.
    '''
    # customer = get_object_or_404(Customer, pk=customer_id)
    # context = { 'customer': customer, }
    context = {}

    return render(request, 'customers/customer_detail.html', context)
