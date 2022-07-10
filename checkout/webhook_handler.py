from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from .models import Invoice, Inv_lineitem
from products.models import Product, Vat_rate
from customers.models import Customer_product

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, invoice):
        """Send the user a confirmation email"""
        cust_email = invoice.customer.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'invoice': invoice})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'invoice': invoice, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""

        intent = event.data.object
        print('+-'*30) # ---------------------- _TODO_ DELETE ME --------------------------- #
        print(intent)
        print('+-'*30)
        customer = intent.metadata.username
        cart = intent.metadata.cart
        cust_ref = intent.metadata.cust_ref
        stripe_pid = intent.id

        invoice_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # has the new invoice been successfully saved yet..?
                invoice = Invoice.objects.get(payment_id=stripe_pid)
                invoice_exists = True
                break
            except Invoice.DoesNotExist:    
                attempt += 1
                time.sleep(1)
        
        if invoice_exists:
            self._send_confirmation_email(invoice)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified invoice already in database'), status=200)
        else:
            # let's try to create the invoice here..
            invoice = None
            try:
                invoice = Invoice.objects.create(
                    customer=customer,
                    cust_ref=cust_ref,
                    payment_id=stripe_pid,
                )
                # iterate through the cart items, add to inv_lineitem
                for item_id, qty in json.loads(cart).items():
                    try:
                        product = get_object_or_404(Product, pk=item_id)
                        vat_rate = Vat_rate.objects.get(
                                                    id=product.def_vat_rate.id)
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
                        )
                        inv_line_item.save()
                        # lastly, add subscrip products to the cust_prod table
                        if product.recurring_bill != 'Z':
                            cust_prod = Customer_product(
                                customer=customer,
                                product=product,
                                qty=qty,
                                bill_freq=product.recurring_bill,
                                next_bill_date=(
                                    Customer_product
                                    ._calc_next_bill_date(
                                    product.recurring_bill)
                                )
                            )
                            cust_prod.save()
                    except Exception as e:
                        if invoice:
                            invoice.delete()
                        return HttpResponse(
                            content=f'Webhook received: \
                                      {event["type"]} | ERROR: {e}',
                                    status=500)

            except Exception as e:
                if invoice:
                    invoice.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                            status=500)

            self._send_confirmation_email(invoice)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                          'Created invoice in webhook'), status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
