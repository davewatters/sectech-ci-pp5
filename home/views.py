from django.shortcuts import render

from products.models import Product


def home(request):
    '''
    Display the main site landing page.
    Promoted prodcuts/services are displayed 
    in descending order, by highest display_rank.
    '''
    # get promoted products, sort by highest rank
    promoted_products = Product.objects.filter(display_rank__gt=0).order_by('-display_rank')

    context = {
        'promoted_products': promoted_products,
    }
    template = 'home.html'
    
    return render(request, template, context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)
