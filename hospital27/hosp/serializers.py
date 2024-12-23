from rest_framework import serializers
from .models import BillingInvoice, InvoiceItem, PaymentTransaction

class InvoiceItemSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = InvoiceItem
        fields = ['service', 'service_name', 'quantity', 'unit_price', 'total_cost']

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'

class BillingInvoiceSerializer(serializers.ModelSerializer):
    invoice_items = InvoiceItemSerializer(many=True, read_only=True)
    payments = PaymentTransactionSerializer(many=True, read_only=True)
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)

    class Meta:
        model = BillingInvoice
        fields = '__all__'