from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import BillingInvoice

@receiver(post_save, sender=BillingInvoice)
def check_invoice_due_status(sender, instance, **kwargs):
    """
    Automatically update invoice status to overdue if past due date
    """
    if instance.payment_status != 'PAID' and instance.due_date < timezone.now():
        instance.payment_status = 'OVERDUE'
        instance.save()