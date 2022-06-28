from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.customer_detail, name='customer-detail'),
]
