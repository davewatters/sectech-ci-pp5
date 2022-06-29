from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import CustomerForm
from .models import Customer


def customer_create(request):
    '''
    View shows new customer form.
    '''
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            messages.success(request, 'Successfully added customer')
            return redirect(reverse('customer-detail', args=[customer.id]))
 
    else:
        form = CustomerForm(request.GET)
        
    template = 'customers/customer_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def customer_detail(request, customer_id):
    '''
    View shows detail of logged-in customer. Allows update.
    Includes views of customer's products and past invoices.
    '''
    account = get_object_or_404(Customer, id=customer_id)

    form = CustomerForm(instance=account)

    if request.method == 'POST':
        pass
    else:
        pass
        
    context = {
        'form': form,
    }

    return render(request, 'customers/customer_detail.html', context)
