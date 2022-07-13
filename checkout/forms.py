from django import forms

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['cust_ref', ]

    def __init__(self, *args, **kwargs):
        """
        Set the placeholder & remove auto-generated label
        """
        super().__init__(*args, **kwargs)
        self.fields['cust_ref'].widget.attrs['placeholder'] = 'Your Ref'
        self.fields['cust_ref'].label = ""
