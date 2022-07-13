from django import template

register = template.Library()


@register.filter
def calc_line_net_amt(price, qty):
    '''
    Calculates the invoice line net cost (total ex vat)
    '''
    return price * qty


@register.filter
def calc_line_vat_amt(line_net, vat_rate):
    '''
    Calculates the invoice line vat amt
    '''
    return line_net * (vat_rate/100)
