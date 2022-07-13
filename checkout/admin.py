from django.contrib import admin
from .models import Invoice, Inv_lineitem


class InvoiceLineItemAdminInline(admin.TabularInline):
    model = Inv_lineitem
    readonly_fields = ('net_cost', 'vat_amt', 'total_cost')


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceLineItemAdminInline,)

    readonly_fields = ('number', 'date',
                       'total_cost', 'vat_amt',
                       'grand_total', 'payment_id')

    fields = ('customer', 'cust_ref',
              'total_cost', 'vat_amt', 'grand_total',)

    list_display = ('number', 'date', 'customer', 'cust_ref',
                    'total_cost', 'vat_amt', 'grand_total')

    ordering = ('-date',)


admin.site.register(Invoice, InvoiceAdmin)
