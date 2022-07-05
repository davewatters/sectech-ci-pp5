from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Invoice

from .forms import InvoiceForm

from customers.models import Customer
from customers.forms import CustomerForm
from shopping_cart.contexts import cart_contents


@login_required
def checkout(request):
    '''
    View that renders the checkout page.
    '''
    cart = request.session.get('cart', {})
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':

        form_data = {
            'cust_ref': request.POST['cust_ref'],
            'vat_no': request.POST['customer.vat_no'],
        }

        inv_form = InvoiceForm(form_data)
        if inv_form.is_valid():
            invoice = inv_form.save(commit=False) 
            # get stripe pid here
            # save to payment_id
            invoice.save()
            # iterate through the cart items
            # add each to inv_lineitem
            # inv_lineitem.save()
            return redirect(reverse('customer-detail', args=[customer.id]))
    else:
        if not cart:
            messages.error(request, "Your shopping cart is empty.")
            return redirect('product-list')

        form_data = {
            # 'vat_no': customer.vat_no,
        }
        inv_form = InvoiceForm(form_data)


    context = {
        'customer': customer,
        'form': inv_form,
    }

    return render(request, 'checkout/checkout.html', context )
