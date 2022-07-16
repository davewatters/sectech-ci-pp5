from django import forms
from .models import Prod_category, Product, Vat_rate


class ProductForm(forms.ModelForm):
    '''Create the proudct form. Use all fields.'''

    # override default empty_label for some fields
    category = forms.ModelChoiceField(
                    queryset=Prod_category.objects.all(),
                    empty_label='-- select product category* --')
    def_vat_rate = forms.ModelChoiceField(
                        queryset=Vat_rate.objects.all(),
                        empty_label='-- select default vat rate* --')

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove auto-generated
        labels and set autofocus on code
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'code': 'Product code',
            'desc': 'Description',
            'long_desc': 'Detailed product description',
            'category': '',
            'sell_price': 'Net sales price',
            'sku': 'Vendor product code',
            'unit': 'Unit',
            'def_vat_rate': '',
        }

        exclude_fields = [
            'image',
            'recurring_bill',
            'display_rank',
            'out_of_use',
        ]

        for field in self.fields:
            if field not in exclude_fields:
                self.fields[field].label = False
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['aria-label'] = placeholder
            self.fields[field].error_messages = {'required': ''}
        self.fields['code'].widget.attrs['autofocus'] = True
