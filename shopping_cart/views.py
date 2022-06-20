from django.shortcuts import render, redirect

from products.models import Product


def view_cart(request):
    '''
    View that renders the contents of the shopping cart.
    '''

    return render(request, 'shopping_cart/cart.html')


# def add_to_cart(request, item_id):
#     '''
#     Adds a product to the shopping cart or 
#     increase it's qty count if product already in cart.
#     '''
#     redirect_url = request.POST.get('redirect_url')

#     return redirect(redirect_url)
