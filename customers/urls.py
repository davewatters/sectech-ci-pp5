from django.urls import path
from . import views

urlpatterns = [
    path('account/new/', views.customer_create, name='customer-create'),
    path('account/<customer_id>/', views.customer_detail, name='customer-detail'),
]
