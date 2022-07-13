from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Define the Customer fields shown in the admin panel.
    '''
    readonly_fields = ('user',)

    list_display = (
        'name',
        'contact',
        'phone_no',
        'town_or_city',
        'country_code',
    )

    ordering = ('-name',)
