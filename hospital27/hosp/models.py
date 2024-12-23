from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Bed(models.Model):
    is_available = models.BooleanField(default=True)








class BedApplication(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Eye_Care(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Dental(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skin_Care(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Physical_Therappy(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=15)
    # Add other doctor-specific fields here

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    # Add other staff-specific fields here

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.position}"



# class Patient(models.Model):
#     """
#     Model representing a patient
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=10, choices=[
#         ('MALE', 'Male'),
#         ('FEMALE', 'Female'),
#         ('OTHER', 'Other')
#     ])
#     contact_number = models.CharField(max_length=15)
#     address = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.user.get_full_name()} (Patient)"


class Disease(models.Model):
    """
    Model representing a disease
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Medicine(models.Model):
    """
    Model representing a medicine
    """
    name = models.CharField(max_length=200, unique=True)
    generic_name = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    CATEGORY_CHOICES = [
        ('cardiac','Cardiac'),
        ('neurologist', 'Neurologist'),
        ('ortho', 'Ortho'),

    ]

    STATUS_CHOICES = [

            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),


    ]


    date = models.DateField()
    department = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=10,
        validators =[
            RegexValidator(
                regex=r'^\d{10}$',  # Only allows 10 digits
                message="Mobile number must be exactly 10 digits.",
                code='invalid_mobile'
            )
        ]
    )

    status = models.CharField(max_length=20,choices = STATUS_CHOICES, default='pending')
    status_notes = models.TextField(blank=True,null=True,help_text="Additional notes about status change")
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)


    def __str__(self):
        return self.name









class Prescription(models.Model):
    """
    Model representing a prescription
    """
    patient = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    date_issued = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.get_full_name()} by Dr. {self.doctor.user.get_full_name()} on {self.date_issued.date()}"




class PrescriptionItem(models.Model):
    """
    Model representing individual items in a prescription
    """
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medicine.name} for {self.disease.name if self.disease else 'Unspecified'}"


class MedicalService(models.Model):
    """
    Model to represent medical services and their pricing
    """
    CATEGORY_CHOICES = [
        ('CONSULTATION', 'Consultation'),
        ('DIAGNOSTIC', 'Diagnostic Test'),
        ('PROCEDURE', 'Medical Procedure'),
        ('TREATMENT', 'Treatment'),
        ('MEDICATION', 'Medication')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    class Meta:
        ordering = ['name']


from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
# from patients.models import Patient
# from services.models import MedicalService


class BillingInvoice(models.Model):
    """
    Model to represent a hospital billing invoice
    """
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('PARTIALLY_PAID', 'Partially Paid'),
        ('OVERDUE', 'Overdue'),
    ]

    patient = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.patient.name}"

    def calculate_total(self):
        """
        Calculate total amount based on invoice items
        """
        invoice_items = self.invoice_items.all()
        self.total_amount = sum(item.total_cost for item in invoice_items)
        self.save()


class InvoiceItem(models.Model):
    """
    Model to represent individual items in an invoice
    """
    invoice = models.ForeignKey(BillingInvoice, related_name='invoice_items', on_delete=models.CASCADE)
    service = models.ForeignKey(MedicalService, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        """
        Calculate total cost before saving
        """
        self.total_cost = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        # Update parent invoice total
        self.invoice.calculate_total()


class PaymentTransaction(models.Model):
    """
    Model to track payment transactions for invoices
    """
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('INSURANCE', 'Insurance'),
        ('ONLINE', 'Online Payment'),
    ]

    invoice = models.ForeignKey(BillingInvoice, related_name='payments', on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Update invoice payment status when transaction is saved
        """
        super().save(*args, **kwargs)
        self.update_invoice_status()

    def update_invoice_status(self):
        """
        Automatically update invoice payment status based on transactions
        """
        total_paid = sum(transaction.amount_paid for transaction in self.invoice.payments.all())

        if total_paid >= self.invoice.total_amount:
            self.invoice.payment_status = 'PAID'
        elif total_paid > 0:
            self.invoice.payment_status = 'PARTIALLY_PAID'
        else:
            self.invoice.payment_status = 'PENDING'

        self.invoice.save()



class PaymentOptions(models.Model):

    email = models.EmailField()
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
