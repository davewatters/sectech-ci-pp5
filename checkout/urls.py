from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cache_checkout_data/',
         views.cache_checkout_data, name='cache-checkout-data'),
    path('success/<invoice_id>',
         views.checkout_success, name='checkout-success'),
    path('wh/', webhook, name='webhook'),
]
