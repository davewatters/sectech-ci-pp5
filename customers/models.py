from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from products.models import Product

class Customer(models.Model):
    '''
    Customer account model.
    Users must have a registered account to buy services.
    Country code is required to process Stripe payments.
    Note: Username & email are linked to in auth_user table.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=32, null=True, blank=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    town_or_city = models.CharField(max_length=255)
    country_code = CountryField(blank_label='Country *')
    postcode = models.CharField(max_length=16, null=True, blank=True)
    vat_no = models.CharField(max_length=16, null=True, blank=True)
    out_of_use = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Customer_product(models.Model):
    '''
    Defines the customer product model. Stores all of the active
    service/software licences & renewal dates owned by this customer.
    '''

    # Billing frequency for recurring licence/subscription services
    RECURRING_BILL = (
        ('A', 'Annual'),
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('B', 'Biennial'),
        ('Z', 'No'),
    )

    customer = models.ForeignKey(Customer,
                                 on_delete=models.PROTECT,
                                 related_name='products')
    product = models.ForeignKey(Product,
                                 on_delete=models.PROTECT,
                                 related_name='customers')
    qty = models.IntegerField(default=0)
    bill_freq = models.CharField(max_length=1,
                                 choices=RECURRING_BILL,
                                 default='Z')
    last_bill_date = models.DateField()
    next_bill_date = models.DateField()

    def __str__(self):
        return f'''{self.product.desc}: 
                   {self.bill_freq.RECURRING_BILL},
                   {self.next_bill_date}'''
