from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Prod_category, Product


class ProductList(generic.ListView):
    '''
    Displays a list of all products
    '''
    model = Product


def product_detail(request, product_id):
    '''
    View shows detail of selected product.
    '''
    product = get_object_or_404(Product, pk=product_id)
    context = { 'product': product, }

    return render(request, 'products/product_detail.html', context)
