from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer

@receiver(post_save, sender=User)
def create_customer_account(sender, instance, created, **kwargs):
    """
    When a new user signs up, insert a customer account record.
    """
    if not instance.is_staff:
        if created:
            Customer.objects.create(user=instance)
