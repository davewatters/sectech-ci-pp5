from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<invoice_id>', views.checkout_success, name='checkout-success'),
]
