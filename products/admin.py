from django.contrib import admin
from .models import Prod_category, Product


@admin.register(Prod_category)
class Prod_categoryAdmin(admin.ModelAdmin):
    '''
    Define the Product Category fields shown in the admin panel.
    '''
    list_display = ('desc', 'disp_name')


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
