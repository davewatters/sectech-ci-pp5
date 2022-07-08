from django import forms
from django.shortcuts import get_object_or_404

from .models import Invoice

from customers.models import Customer


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['cust_ref',]

    def __init__(self, *args, **kwargs):
        """
        Set the placeholder & remove auto-generated label
        """
        super().__init__(*args, **kwargs)
        self.fields['cust_ref'].widget.attrs['placeholder'] = 'Your Ref'
        # self.fields['cust_ref'].widget.attrs['class'] = 'stripe-style-input'
        self.fields['cust_ref'].label = ""
