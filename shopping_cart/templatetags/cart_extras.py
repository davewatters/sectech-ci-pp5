from django import template

register = template.Library()

@register.filter
def calc_linetotal(price, qty):
    '''
    Calculates the order line total
    '''
    return price * qty
