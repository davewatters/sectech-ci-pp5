# Hook into the user login mechanism to override default behaviour
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects
from django.conf import settings
from django.contrib import messages
from django.shortcuts import resolve_url

from allauth.account.adapter import DefaultAccountAdapter

from .models import Customer


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom mod to override default redirect behaviour at login.
    Related: settings.ACCOUNT_ADAPTER
    """

    def get_login_redirect_url(self, request):
        '''
        Returns the default URL to redirect to after logging in.
        '''
        url = resolve_url(settings.LOGIN_REDIRECT_URL)

        # if user is a customer check if we have account details,
        # if not (first time login), override default redirect url to
        # present customer account details form.
        if not request.user.is_staff:
            if Customer.objects.filter(user=request.user).exists():
                print('-*'*20)
                print(Customer)
                print(Customer.objects.name)
                if not Customer.name:
                    messages.warning(request,
                        f'Welcome {request.user.email}: You will need to provide \
                        full customer account details.')
                url = resolve_url('customer-create')

        return url

