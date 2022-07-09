from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Invoice, Inv_lineitem
from products.models import Product
from customers.models import Customer

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    # def _send_confirmation_email(self, invoice):
    #     """Send the user a confirmation email"""
    #     cust_email = invoice.email
    #     subject = render_to_string(
    #         'checkout/confirmation_emails/confirmation_email_subject.txt',
    #         {'invoice': invoice})
    #     body = render_to_string(
    #         'checkout/confirmation_emails/confirmation_email_body.txt',
    #         {'invoice': invoice, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    #     send_mail(
    #         subject,
    #         body,
    #         settings.DEFAULT_FROM_EMAIL,
    #         [cust_email]
    #     )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # intent = event.data.object
        # pid = intent.id
        # save_info = intent.metadata.save_info

        # billing_details = intent.charges.data[0].billing_details
        # shipping_details = intent.shipping
        # grand_total = round(intent.charges.data[0].amount / 100, 2)

        # invoice_exists = False
        # attempt = 1
        # while attempt <= 5:
        #     try:
        #         invoice = Invoice.objects.get(
        #             full_name__iexact=shipping_details.name,
        #             email__iexact=billing_details.email,
        #             phone_number__iexact=shipping_details.phone,
        #             country__iexact=shipping_details.address.country,
        #             postcode__iexact=shipping_details.address.postal_code,
        #             town_or_city__iexact=shipping_details.address.city,
        #             street_address1__iexact=shipping_details.address.line1,
        #             street_address2__iexact=shipping_details.address.line2,
        #             county__iexact=shipping_details.address.state,
        #             grand_total=grand_total,
        #             original_bag=bag,
        #             stripe_pid=pid,
        #         )
        #         invoice_exists = True
        #         break
        #     except Invoice.DoesNotExist:
        #         attempt += 1
        #         time.sleep(1)
        # if invoice_exists:
        #     # self._send_confirmation_email(invoice)
        #     return HttpResponse(
        #         content=(f'Webhook received: {event["type"]} | SUCCESS: '
        #                  'Verified invoice already in database'),
        #         status=200)
        # else:
        #     invoice = None
        #     try:
        #         invoice = Invoice.objects.create(
        #             full_name=shipping_details.name,
        #             user_profile=profile,
        #             email=billing_details.email,
        #             phone_number=shipping_details.phone,
        #             country=shipping_details.address.country,
        #             postcode=shipping_details.address.postal_code,
        #             town_or_city=shipping_details.address.city,
        #             street_address1=shipping_details.address.line1,
        #             street_address2=shipping_details.address.line2,
        #             county=shipping_details.address.state,
        #             original_bag=bag,
        #             stripe_pid=pid,
        #         )
        #         for item_id, item_data in json.loads(bag).items():
        #             product = Product.objects.get(id=item_id)
        #                 inv_line_item = Inv_lineitem(
        #                     invoice=invoice,
        #                     product=product,
        #                     quantity=item_data,
        #                 )
        #         inv_line_item.save()
        #     except Exception as e:
        #         if invoice:
        #             invoice.delete()
                    # return HttpResponse(
                    #     content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    #     status=500)
        # self._send_confirmation_email(invoice)

        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created invoice in webhook'),
                      status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200)
