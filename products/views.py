from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ProductForm
from .models import Product


@login_required
def product_create(request):
    '''View to create a new product.'''

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request,
                             f'Successfully added product {product.desc}')
            return redirect('product-list')
    else:
        form = ProductForm(request.GET)

    context = {'form': form, }
    template = 'products/product_form.html'
    return render(request, template, context)


def product_list(request):
    '''
    Display list of all products
    '''
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    template = 'products/product_list.html'
    return render(request, template, context)


def product_detail(request, product_id):
    '''
    View to display the selected product.
    '''
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def product_delete(request, product_id):
    '''
    View to allow only site admin to delete a product record.
    '''
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'Unauthorized to view that product page.')
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
    context = {
        'product': product,
    }
    return render(request, 'products/product_confirm_delete.html', context)


@login_required
def product_update(request, product_id):
    '''View to update a product.'''

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request,
                             f'Successfully updated product {product.desc}')
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
    }
    return render(request, 'products/product_update.html', context)
