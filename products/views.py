from django.shortcuts import render, get_object_or_404

from .models import Product


# class ProductList(generic.ListView):
#     '''
#     Displays a list of all products
#     '''
#     model = Product

def product_list(request):
    '''
    Display list of all products
    '''
    product_list = Product.objects.all()

    context = {'product_list': product_list, }
    template = 'products/product_list.html'

    return render(request, template, context)


def product_detail(request, product_id):
    '''
    View shows detail of selected product.
    '''
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product, }

    return render(request, 'products/product_detail.html', context)
