from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def my_check_on_login(request, user, **kwargs):
    """
    When the user logs in check to see if customer has details
    """
    print('*--'*20)
    print('Signal: User has just logged in')
    print('*--'*20)
