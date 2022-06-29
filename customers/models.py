from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


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

    def __str__(self):
        return self.name
