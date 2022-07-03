# Hook into the user login mechanism to override default behaviour
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects
from django.conf import settings
from django.contrib import messages
from django.shortcuts import resolve_url

from allauth.account.adapter import DefaultAccountAdapter

from .models import Customer

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom mod to override default allauth redirect behaviour at login.
    Related: settings.ACCOUNT_ADAPTER
    """

    def get_login_redirect_url(self, request):
        '''
        Returns the default URL to redirect to after logging in.
        We want first time users to fill in their business details.
        '''
        url = resolve_url(settings.LOGIN_REDIRECT_URL)

        # if user is a customer and we don't yet have required account details
        # (i.e. first time login), override default redirect url to
        # present customer account details form.
        if not request.user.is_staff:
            if Customer.objects.filter(user=request.user, name='').exists():
                messages.warning(request,
                    f'Welcome {request.user.email}! Plesae provide \
                    full customer account details to complete your \
                    registration.')
                url = resolve_url('customer-create')

        return url
