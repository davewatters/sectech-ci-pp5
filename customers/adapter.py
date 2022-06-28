# Hook into the user login mechanism to override default behaviour
# https://django-allauth.readthedocs.io/en/latest/advanced.html#custom-redirects
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        print('*--'*20)
        print('Adapter: User has just logged in')
        print('*--'*20)
        path = "/customers/{username}/"
        return path.format(username=request.user.username)
