from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from .forms import CustomerForm
from .models import Customer, Customer_product


@login_required
def customer_create(request):
    '''View shows new customer form'''
    customer = get_object_or_404(Customer, user=request.user.id)

    # stop user access by typing url
    if customer.name:
        messages.error(request, 'Customer already setup.')
        return redirect('customer-detail', customer.id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            customer = form.save()
            messages.success(request,
                             f'Successfully added customer {customer.name}')
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
    # Customer record can only be opened by correct user
    if request.user.id != customer.user_id:
        messages.error(request, 'Unauthorized to view that customer page.')
        return redirect(settings.LOGIN_REDIRECT_URL)
        # return HttpResponse(status=403)

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
