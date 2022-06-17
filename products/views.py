from django.shortcuts import render
from django.views import generic, View

from .models import Prod_category, Product


class ProductList(generic.ListView):
    '''
    Displays a list of all products
    '''
    model = Product

