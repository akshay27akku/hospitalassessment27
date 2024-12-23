from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import Appointments, EyeCareForm, DentalForm, SkinCareForm, Physical_TherappyForm
from django.contrib import messages
# from .forms import BedApplicationForm
from .models import Appointment, Eye_Care, Dental, Skin_Care, Physical_Therappy, Prescription


# Create your views here.
def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def department(request):
    return render(request, 'department.html')


def doctors(request):
    return render(request, 'doctors.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def appointment_view(request):
    if request.method == 'POST':
        form = Appointments(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Appointments()

    return render(request, 'appointment.html', {'form': form})


# def appointment_list(request):
#     appointments = Appointment.objects.all()
#     return render(request,'appointment_list.html',{'appointments':appointments})
#     bed_lists = BedApplication.objects.all()
#     return render(request, 'bed_list.html', {'bed_lists': bed_lists})


def success(request):
    return render(request, 'success.html')


def contact_us(request):
    context = {'phone_number': 7594091773}
    return render(request, 'contact_us.html', context)


# views.py
from django.shortcuts import render, redirect
from .models import Bed, BedApplication
from .forms import BedApplicationForm


def apply_for_bed(request):
    # Count total beds
    total_beds = Bed.objects.count()

    # Count available beds
    available_beds = Bed.objects.filter(is_available=True).count()

    if available_beds == 0:
        return render(request, 'apply_for_bed.html', {
            'total_beds': total_beds,
            'available_beds': available_beds,
            'message': 'No beds are available.'
        })

    if request.method == 'POST':
        form = BedApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Update a bed to unavailable after a successful application
            bed = Bed.objects.filter(is_available=True).first()
            if bed:
                bed.is_available = False
                bed.save()

            # Recount available beds after application
            available_beds = Bed.objects.filter(is_available=True).count()

            return render(request, 'apply_for_bed.html', {
                'total_beds': total_beds,
                'available_beds': available_beds,
                'message': 'Application submitted successfully!'
            })
    else:
        form = BedApplicationForm()

    return render(request, 'apply_for_bed.html', {
        'form': form,
        'total_beds': total_beds,
        'available_beds': available_beds
    })


# def bed_list(request):
#     bed_lists = BedApplication.objects.all()
#     return render(request,'bed_list.html',{'bed_lists':bed_lists})










def eye_care_view(request):
    if request.method == 'POST':
        form = EyeCareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EyeCareForm()

    return render(request, 'Eye_Care.html', {'form': form})


def eye_care_template(request):
    return render(request,'eye_care_template.html')



def dental_view(request):
    if request.method == 'POST':
        form = DentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DentalForm()

    return render(request, 'Dental.html', {'form': form})




def dental_template(request):
    return render(request,'dental_template.html')




def skin_care_view(request):
    if request.method == 'POST':
        form = SkinCareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SkinCareForm()

    return render(request, 'Skin_Care.html', {'form': form})


def skin_care_template(request):
    return render(request,'skin_care_template.html')



def physical_therappy_view(request):
    if request.method == 'POST':
        form = Physical_TherappyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Physical_TherappyForm()

    return render(request, 'physical_therappy.html', {'form': form})


def physical_therappy_template(request):
    return render(request,'physical_therappy_template.html')


def diagnostic_view(request):
    return render(request,'diagnostic.html')


def surgery_service_view(request):
    return render(request,'surgery_service.html')



from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Doctor, Staff

def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')  # 'doctor' or 'staff'
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        additional_field = request.POST.get('additional_field')# specialization/department, etc.
        additional_field2 = request.POST.get('additional_field2')


        # Create User
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,)

        # Add to Doctor or Staff table
        if role == 'doctor':
            Doctor.objects.create(user=user, specialization=additional_field,experience=additional_field2)
        elif role == 'staff':
            Staff.objects.create(user=user, department=additional_field,position=additional_field2)

        return redirect('login')  # Redirect to login after registration

    return render(request, 'register.html')



from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    def get_success_url(self):
        if hasattr(self.request.user, 'doctor'):
            return '/doctor_dashboard/'
        elif hasattr(self.request.user, 'staff'):
            return '/staff_dashboard/'
        else:
            return '/dashboard/'  # Default redirect




from django.contrib.auth.decorators import login_required

@login_required

def staff_dashboard_view(request):
    if not hasattr(request.user, 'staff'):
        return render(request, 'error.html', {'message': 'Unauthorized access'})

    appointments = Appointment.objects.all()
    bed_lists = BedApplication.objects.all()
    eye_care_patients = Eye_Care.objects.all()
    dental_patients = Dental.objects.all()
    skin_care_patients = Skin_Care.objects.all()
    physical_therappy_patients = Physical_Therappy.objects.all()

    combined_patients = []

    for patient in eye_care_patients:
        combined_patients.append({
            'patient':patient,
            'service_type':'Eye Care'
        })

    for patient in dental_patients:
        combined_patients.append({
            'patient':patient,
            'service_type':'Dental'
        })

    for patient in skin_care_patients:
        combined_patients.append({
            'patient':patient,
            'service_type':'Skin Care'
        })

    for patient in physical_therappy_patients:
        combined_patients.append({
            'patient':patient,
            'service_type':'Physical Therappy'
        })


    return render(request, 'staff_dashboard.html', {'staff': request.user.staff,'appointments':appointments,'bed_lists':bed_lists,'combined_patients':combined_patients})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q


@login_required
def doctor_dashboard(request):
    # Check if the logged-in user is a doctor
    if not hasattr(request.user, 'doctor'):
        return render(request, 'error.html', {'message': 'Unauthorized access'})

    # Get the current doctor
    current_doctor = request.user.doctor
    # print(f"Doctor:{current_doctor},Name:{current_doctor.name}")
    # Filter appointments specifically for this doctor
    appointments = Appointment.objects.filter(
        Q(doctor=current_doctor) |
        Q(doctor__isnull=True)  # Optional: include unassigned appointments
    ).order_by('-created_at')  # Assuming you have a created_at field
    doctor_name = current_doctor.name
    # Get some additional context if needed
    total_appointments = appointments.count()
    pending_appointments = appointments.filter(status='pending').count()


    context = {
        'doctor': current_doctor,
        'appointments': appointments,
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'doctor_name': current_doctor.name,

    }

    return render(request, 'doctor_dashboard.html', context)






from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Appointment


@login_required
def appointment_detail(request, appointment_id):
    # Fetch the specific appointment
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Permission check
    # If the user is a doctor, they should only see their own appointments
    if hasattr(request.user, 'doctor'):
        if appointment.doctor != request.user.doctor:
            raise PermissionDenied("You do not have permission to view this appointment.")

    # If the user is staff, they can view all appointments
    elif not hasattr(request.user, 'staff'):
        raise PermissionDenied("You do not have permission to view this appointment.")

    context = {
        'appointment': appointment,
    }

    return render(request, 'appointment_detail.html', context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


@login_required
def update_appointment_status(request, appointment_id):
    # Ensure only doctors or staff can update status
    if not (hasattr(request.user, 'doctor') or hasattr(request.user, 'staff')):
        raise PermissionDenied("You do not have permission to update appointment status.")
    #
    appointment = get_object_or_404(Appointment, id=appointment_id)
    #
    # # Permission check for doctors
    if hasattr(request.user, 'doctor') and appointment.doctor != request.user.doctor:
        raise PermissionDenied("You can only update your own appointments.")

    if request.method == 'POST':
        new_status = request.POST.get('status')
        notes = request.POST.get('notes', '').strip()
        if new_status in dict(Appointment.STATUS_CHOICES):
            appointment.status = new_status
            appointment.save()
            messages.success(request, "Appointment status updated successfully.")
            return redirect('appointment_detail', appointment_id=appointment.id)
        else:
            messages.error(request,"Invalid status selected.")

    # If GET request, show status update form
    return render(request, 'update_appointment_status.html', {
        'appointment': appointment,
        'status_choices': appointment.STATUS_CHOICES
    })



# def staff_dashboard(request):
#     messages.success(request,"successfully logined")
#
#     return render(request,'staff_dashboard.html')
#
# def doctor_dashboard(request):
#     messages.success(request,"successfully loginned")


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PrescriptionForm, PrescriptionItemFormSet


@login_required
def create_prescription(request):
    """
    View to create a new prescription
    """
    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        prescription_item_formset = PrescriptionItemFormSet(request.POST)

        if prescription_form.is_valid() and prescription_item_formset.is_valid():
            # Save prescription
            prescription = prescription_form.save(commit=False)
            prescription.doctor = request.user.doctor  # Assuming user is logged in as a doctor
            prescription.save()

            # Save prescription items
            prescription_items = prescription_item_formset.save(commit=False)
            for item in prescription_items:
                item.prescription = prescription
                item.save()

            messages.success(request, 'Prescription created successfully!')
            return redirect('prescription_detail', pk=prescription.pk)
    else:
        prescription_form = PrescriptionForm()
        prescription_item_formset = PrescriptionItemFormSet()

    return render(request, 'prescriptions/create_prescription.html', {
        'prescription_form': prescription_form,
        'prescription_item_formset': prescription_item_formset
    })

# @login_required
# def create_prescription(request):
#     """
#     View to create a new prescription with comprehensive error handling
#     """
#     if request.method == 'POST':
#         prescription_form = PrescriptionForm(request.POST)
#         prescription_item_formset = PrescriptionItemFormSet(request.POST)
#
#         # Debug print statements to help diagnose issues
#         print("Prescription Form Errors:", prescription_form.errors)
#         print("Prescription Item Formset Errors:", prescription_item_formset.errors)
#         print("Prescription Form is Valid:", prescription_form.is_valid())
#         print("Prescription Item Formset is Valid:", prescription_item_formset.is_valid())
#
#         if prescription_form.is_valid():
#             if prescription_item_formset.is_valid():
#                 try:
#                     # Save prescription
#                     prescription = prescription_form.save(commit=False)
#                     prescription.doctor = request.user.doctor  # Assuming user is logged in as a doctor
#                     prescription.save()
#
#                     # Save prescription items
#                     prescription_items = prescription_item_formset.save(commit=False)
#
#                     # Check if there are any prescription items
#                     if not prescription_items:
#                         messages.warning(request, 'Please add at least one prescription item.')
#                         return render(request, 'prescriptions/create_prescription.html', {
#                             'prescription_form': prescription_form,
#                             'prescription_item_formset': prescription_item_formset
#                         })
#
#                     for item in prescription_items:
#                         item.prescription = prescription
#                         item.save()
#
#                     messages.success(request, 'Prescription created successfully!')
#                     return redirect('prescription_detail', pk=prescription.pk)
#
#                 except Exception as e:
#                     # Catch and log any unexpected errors during save
#                     messages.error(request, f'An error occurred: {str(e)}')
#                     print(f"Error saving prescription: {e}")
#             else:
#                 # If prescription item formset is invalid, show error messages
#                 messages.error(request, 'Please correct the errors in the prescription items.')
#         else:
#             # If prescription form is invalid, show error messages
#             messages.error(request, 'Please correct the errors in the prescription form.')
#
#     else:
#         # GET request: initialize empty forms
#         prescription_form = PrescriptionForm()
#         prescription_item_formset = PrescriptionItemFormSet()
#
#     return render(request, 'prescriptions/create_prescription.html', {
#         'prescription_form': prescription_form,
#         'prescription_item_formset': prescription_item_formset
#     })
@login_required
def prescription_detail(request, pk):
    """
    View to display prescription details
    """
    prescription = get_object_or_404(Prescription, pk=pk)

    # Check if the user has permission to view (doctor or patient)
    if (not hasattr(request.user, 'doctor') and
            not hasattr(request.user, 'patient') or
            (hasattr(request.user, 'doctor') and prescription.doctor != request.user.doctor) or
            (hasattr(request.user, 'patient') and prescription.patient != request.user.patient)):
        messages.error(request, 'You do not have permission to view this prescription.')
        return redirect('home')

    return render(request, 'prescriptions/prescription_detail.html', {
        'prescription': prescription
    })


@login_required
def patient_prescriptions(request):
    """
    View to list prescriptions for a patient
    """
    try:
        patient = request.user.patient
        prescriptions = patient.prescriptions.all().order_by('-date_issued')
        return render(request, 'prescriptions/patient_prescriptions.html', {
            'prescriptions': prescriptions
        })
    except Appointment.DoesNotExist:
        messages.error(request, 'Patient profile not found.')
        return redirect('index')


@login_required
def doctor_prescriptions(request):
    """
    View to list prescriptions for a doctor
    """
    try:
        doctor = request.user.doctor
        prescriptions = doctor.prescriptions.all().order_by('-date_issued')
        return render(request, 'prescriptions/doctor_prescriptions.html', {
            'prescriptions': prescriptions
        })
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor profile not found.')
        return redirect('index')


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BillingInvoice, InvoiceItem, PaymentTransaction
from .serializers import BillingInvoiceSerializer, PaymentTransactionSerializer


class BillingInvoiceViewSet(viewsets.ModelViewSet):
    queryset = BillingInvoice.objects.all()
    serializer_class = BillingInvoiceSerializer

    @action(detail=True, methods=['POST'])
    def add_payment(self, request, pk=None):
        """
        Add a payment transaction to an existing invoice
        """
        invoice = self.get_object()
        serializer = PaymentTransactionSerializer(data=request.data)

        if serializer.is_valid():
            payment = serializer.save(invoice=invoice)
            return Response(PaymentTransactionSerializer(payment).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def overdue_invoices(self, request):
        """
        Retrieve all overdue invoices
        """
        overdue_invoices = BillingInvoice.objects.filter(
            payment_status='OVERDUE',
            due_date__lt=timezone.now()
        )
        serializer = self.get_serializer(overdue_invoices, many=True)
        return Response(serializer.data)


from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q

from .models import BillingInvoice, InvoiceItem, PaymentTransaction
from .models import Appointment
from .models import MedicalService


class BillingInvoiceListView(LoginRequiredMixin, ListView):
    """
    View to list all billing invoices with filtering capabilities
    """
    model = BillingInvoice
    template_name = 'billing/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10

    def get_queryset(self):
        """
        Allow filtering of invoices by status
        """
        queryset = super().get_queryset().order_by('-created_at')
        status = self.request.GET.get('status')

        if status:
            queryset = queryset.filter(payment_status=status)

        return queryset


class BillingInvoiceDetailView(LoginRequiredMixin, DetailView):
    """
    View to display detailed information about a specific invoice
    """
    model = BillingInvoice
    template_name = 'billing/invoice_detail.html'
    context_object_name = 'invoice'

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the view
        """
        context = super().get_context_data(**kwargs)
        context['invoice_items'] = self.object.invoice_items.all()
        context['payments'] = self.object.payments.all()
        return context


class AddPaymentView(LoginRequiredMixin, CreateView):
    """
    View to add a payment to an existing invoice
    """
    model = PaymentTransaction
    template_name = 'billing/add_payment.html'
    fields = ['amount_paid', 'payment_method', 'transaction_id']

    def get_context_data(self, **kwargs):
        """
        Add invoice and remaining balance to context
        """
        context = super().get_context_data(**kwargs)
        invoice = get_object_or_404(BillingInvoice, pk=self.kwargs['invoice_id'])

        # Calculate remaining balance
        total_paid = sum(payment.amount_paid for payment in invoice.payments.all())
        remaining_balance = invoice.total_amount - total_paid

        context['invoice'] = invoice
        context['remaining_balance'] = remaining_balance
        return context

    def form_valid(self, form):
        """
        Associate payment with the specific invoice
        """
        invoice = get_object_or_404(BillingInvoice, pk=self.kwargs['invoice_id'])

        # Check if payment amount exceeds remaining balance
        total_paid = sum(payment.amount_paid for payment in invoice.payments.all())
        remaining_balance = invoice.total_amount - total_paid

        if form.cleaned_data['amount_paid'] > remaining_balance:
            form.add_error('amount_paid', 'Payment amount cannot exceed remaining balance')
            return self.form_invalid(form)

        # Save payment and associate with invoice
        form.instance.invoice = invoice
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to invoice detail after successful payment
        """
        return reverse_lazy('invoice-detail', kwargs={'pk': self.kwargs['invoice_id']})


def create_invoice(request):
    """
    View to create a new invoice
    """
    if request.method == 'POST':
        # Extract form data
        patient_id = request.POST.get('patient')

        service_ids = request.POST.getlist('services')


        # Validate data
        try:
            patient = Appointment.objects.get(id=patient_id)
            services = MedicalService.objects.filter(id__in=service_ids)

            total_amount = sum(service.price for service in services)

            # Create invoice
            invoice = BillingInvoice.objects.create(
                patient=patient,
                invoice_number=f'INV-{timezone.now().strftime("%Y%m%d%H%M%S")}',
                due_date=timezone.now() + timezone.timedelta(days=30),
                total_amount = total_amount
            )

            # Create invoice items
            for service in services:
                InvoiceItem.objects.create(
                    invoice=invoice,
                    service=service,
                    quantity=1,
                    unit_price=service.price,
                    total_cost=service.price
                )

            # Calculate total
            invoice.calculate_total()

            return redirect('invoice-detail', pk=invoice.id)

        except Exception as e:
            # Handle errors
            return render(request, 'billing/create_invoice.html', {
                'error': str(e),
                'patients': Appointment.objects.all(),
                'services': MedicalService.objects.all()
            })

    # GET request: show form to create invoice
    return render(request, 'billing/create_invoice.html', {
        'patients': Appointment.objects.all(),
        'services': MedicalService.objects.all()
    })


def overdue_invoices(request):
    """
    View to list overdue invoices
    """
    overdue_invoices = BillingInvoice.objects.filter(
        payment_status='OVERDUE',
        due_date__lt=timezone.now()
    )

    return render(request, 'billing/overdue_invoices.html', {
        'invoices': overdue_invoices
    })