from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomerForm
from .models import Customer, Customer_product


@login_required
def customer_create(request):
    '''View shows new customer form'''
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Successfully added customer {customer.name}')
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CustomerForm(request.GET)

    template = 'customers/customer_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def customer_detail(request, customer_id):
    '''
    View shows account detail of logged-in customer.
    Allows user to update details.
    Includes views of customer's products and past invoices.
    '''
    customer = get_object_or_404(Customer, id=customer_id)
    cust_products = Customer_product.objects.filter(customer=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Customer {customer.name} updated.')
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
        'customer_products': cust_products,
    }

    return render(request, 'customers/customer_detail.html', context)
