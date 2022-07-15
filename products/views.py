from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import Product


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
    View to display the selected product.
    '''
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product, }

    return render(request, 'products/product_detail.html', context)


@login_required
def product_delete(request, product_id):
    '''
    View to allow only site admin to delete a product record.
    '''
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'Unauthorized to view that customer page.')
        return redirect('product-list')

    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            messages.success(request,
                             f'Product {product.desc} successfully deleted.')
        except Exception:
            messages.error(request, f'Can\'t delete product {product.desc} \
                           due to existing dependencies.')
        return redirect('product-list')

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product, }

    return render(request, 'products/product_confirm_delete.html', context)
