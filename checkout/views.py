from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from checkout.models import Invoice, Inv_lineitem
from customers.models import Customer, Customer_product
from products.models import Product, Vat_rate
from sectech import settings 
from shopping_cart.contexts import cart_contents

from .forms import InvoiceForm

import stripe

@login_required
def checkout(request):
    '''
    View to render the checkout page. Processes Stripe card payments.
    '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    customer = get_object_or_404(Customer, user=request.user.id)

    if request.method == 'POST':

        form_data = {
            'cust_ref': request.POST['cust_ref'],
        }

        inv_form = InvoiceForm(form_data)
        if inv_form.is_valid():
            invoice = inv_form.save(commit=False)
            invoice.customer = customer
            # process payment, get stripe pid
            # save to payment_id
            invoice.save()
            # iterate through the cart items, add to inv_lineitem
            for item_id, qty in cart.items():
                product = get_object_or_404(Product, pk=item_id)
                vat_rate = Vat_rate.objects.get(id=product.def_vat_rate.id)
                line_amt = qty * product.sell_price
                line_vat = line_amt * (vat_rate.rate/100)
                total_line = line_amt + line_vat
                inv_line_item = Inv_lineitem(
                    invoice=invoice,
                    product=product,
                    price=product.sell_price,
                    qty=qty,
                    net_cost=line_amt,
                    vat_code=vat_rate.code,
                    vat_rate=vat_rate.rate,
                    vat_amt=line_vat,
                    total_cost=total_line,
                    # payment_id=stripe_pid,
                )
                inv_line_item.save()
                # lastly, add subscription products to the cust product table
                if product.recurring_bill != 'Z':
                    cust_prod = Customer_product(
                        customer=customer,
                        product=product,
                        qty=qty,
                        bill_freq=product.recurring_bill,
                        next_bill_date=Customer_product._calc_next_bill_date(
                                                        product.recurring_bill)
                    )
                    cust_prod.save()
            
            #  Success! Clear the cart
            del request.session['cart']
            return redirect(reverse('checkout-success', args=[invoice.id]))
    else:
        if not cart:
            messages.error(request, "Your shopping cart is empty.")
            return redirect('product-list')

        this_cart = cart_contents(request)
        amt_due = this_cart['grand_total']
        stripe_total = round(amt_due * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        inv_form = InvoiceForm()

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))
        return redirect('view-cart')

    context = {
        'customer': customer,
        'form': inv_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


@login_required
def checkout_success(request, invoice_id):
    '''
    View that renders the checkout success page. Shows the invoice
    details and the payment reference.
    '''
    invoice = get_object_or_404(Invoice, id=invoice_id)
    customer = get_object_or_404(Customer, user=request.user.id)

    messages.warning(request, f'Order successfully Processed. \
        Your invoice number is {invoice.number}.\nA confirmation \
        email will be sent to {request.user.email}.')

    context = {
        'invoice': invoice,
        'customer': customer,
    }
    return render(request, 'checkout/checkout_success.html', context)
