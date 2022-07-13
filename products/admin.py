from django.contrib import admin
from .models import Prod_category, Product, Vat_rate


@admin.register(Prod_category)
class Prod_categoryAdmin(admin.ModelAdmin):
    '''
    Define the Product Category fields shown in the admin panel.
    '''
    list_display = ('desc', 'disp_name')


@admin.register(Vat_rate)
class Vat_rateAdmin(admin.ModelAdmin):
    '''
    Define the VAT Rate fields shown in the admin panel.
    '''
    list_display = ('code', 'rate', 'is_default', 'is_active')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Define the Product fields shown in the admin panel.
    '''
    list_display = (
        'code',
        'desc',
        'category',
        'recurring_bill',
        'sell_price',
    )
