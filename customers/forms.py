from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on business name field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Business Name',
            'contact': 'Primary Contact Person',
            'phone_no': 'Contact Phone Number',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'vat_no': 'VAT Number',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country_code':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                    # self.fields[field].widget.attrs['requied'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
