from django.contrib import admin

from hosp.models import Appointment, Bed, BedApplication, Eye_Care, Dental, Skin_Care, Doctor, Staff, Disease, Medicine, \
    MedicalService

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Bed)
admin.site.register(BedApplication)
admin.site.register(Eye_Care)
admin.site.register(Dental)
admin.site.register(Skin_Care)
admin.site.register(Disease)
admin.site.register(Medicine)
# admin.site.register(Patients)
admin.site.register(MedicalService)


from django.contrib import admin
from .models import Doctor, Staff

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position')

from django.contrib import admin
from .models import BillingInvoice, InvoiceItem, PaymentTransaction

@admin.register(BillingInvoice)
class BillingInvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'patient', 'total_amount', 'payment_status', 'due_date']
    list_filter = ['payment_status', 'due_date']
    search_fields = ['invoice_number', 'patient__full_name']

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'service', 'quantity', 'unit_price', 'total_cost']

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'amount_paid', 'payment_date', 'payment_method']
    list_filter = ['payment_method', 'payment_date']