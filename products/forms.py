from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    '''Create teh proudct form. Use all fields.'''
    class Meta:
        model = Product
        fields = '__all__'
