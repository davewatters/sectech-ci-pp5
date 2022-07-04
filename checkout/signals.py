from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Invoice, Inv_lineitem


@receiver(post_save, sender=Inv_lineitem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.invoice.update_totals()


@receiver(post_delete, sender=Inv_lineitem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.invoice.update_totals()


@receiver(post_save, sender=Invoice)
def save_inv_number(sender, instance, created, **kwargs):
    """
    When a new invoice is created we need to save our unique human-readable
    sales invoice reference number. We are using the model's pk to generate
    this ref so we must call post_save to access the Autofield invoice.id
    """
    if created:
        instance.number = instance._generate_invoice_number()
        instance.save()
