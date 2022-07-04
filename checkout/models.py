from django.db import models
from django.contrib.auth.models import User

from customers.models import Customer
from products.models import Product, Vat_rate

class Invoice(models.Model):
    '''
    Defines the invoice header table. Invoice details are in
    the invoice line item table - one record for each product bought.
    '''
    number = models.CharField(max_length=32, unique=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.PROTECT,
                                 related_name='invoices')
    date = models.DateTimeField(auto_now_add=True)
    cust_ref = models.CharField(max_length=16, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2,
                                     default=0.0)
    vat_amt = models.DecimalField(max_digits=8, decimal_places=2,
                                  default=0.0)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2,
                                     default=0.0)
    payment_id = models.CharField(max_length=255, null=False, blank=False, default='')

    def __str__(self):
        return f'{self.number}: {self.customer}'


class Inv_lineitem(models.Model):
    '''
    Defines the invoice line itmes. Each item must store VAT rate, 
    VAT amount, product price at time of sale. 
    '''
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,
                                related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                related_name='invoices')
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                default=0.0)
    qty = models.IntegerField(default=0)
    net_cost = models.DecimalField(max_digits=8, decimal_places=2,
                                   default=0.0)
    vat_code = models.ForeignKey(Vat_rate, on_delete=models.PROTECT,
                                related_name='inv_items')
    vat_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    vat_amt = models.DecimalField(max_digits=8, decimal_places=2,
                                  default=0.0)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2,
                                     default=0.0)

