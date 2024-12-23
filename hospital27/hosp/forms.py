from django import forms
from .models import Appointment, Eye_Care, Dental, Skin_Care, Staff, Doctor, Physical_Therappy, PrescriptionItem, \
    PaymentOptions
from django.forms.widgets import SelectDateWidget
# from .models import BedApplication
import datetime

class Appointments(forms.ModelForm):
    TIME_CHOICES = [
        ('09:00:00', '9:00 AM'),
        ('10:00:00', '10:00 AM'),
        ('11:00:00', '11:00 AM'),
        ('12:00:00', '12:00 AM'),
        ('01:00:00', '01:00 PM'),
        ('03:00:00', '03:00 PM'),
        ('04:00:00', '04:00 PM'),
        ('05:00:00', '05:00 PM'),
        ('06:00:00', '06:00 PM'),
        ('07:00:00', '07:00 PM'),
        ('08:00:00', '08:00 PM'),
        ('09:00:00', '09:00 PM'),
        ('10:00:00', '10:00 PM'),
        ('11:00:00', '11:00 PM'),

    ]
    time = forms.ChoiceField(choices=TIME_CHOICES, label="Time")
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets={
            'date':SelectDateWidget(years=range(2020,2031)),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': "Time"}),
            'doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': "Doctor"}),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': "Department"}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Mobile"}),
        }


# forms.py
from django import forms
from .models import BedApplication

class BedApplicationForm(forms.ModelForm):
    class Meta:
        model = BedApplication
        fields = ['name', 'age', 'address', 'mobile_number']


class EyeCareForm(forms.ModelForm):
    class Meta:
        model = Eye_Care
        fields = ['name', 'age', 'address', 'mobile_number']


class DentalForm(forms.ModelForm):
    class Meta:
        model = Dental
        fields = ['name', 'age', 'address', 'mobile_number']


class SkinCareForm(forms.ModelForm):
    class Meta:
        model = Skin_Care
        fields = ['name', 'age', 'address', 'mobile_number']


class Physical_TherappyForm(forms.ModelForm):
    class Meta:
        model = Physical_Therappy
        fields = ['name', 'age', 'address', 'mobile_number']


from django import forms
from django.forms import inlineformset_factory
from .models import Prescription,PrescriptionItem,Appointment, Doctor, Disease, Medicine

class PrescriptionForm(forms.ModelForm):
    """
    Form for creating a new prescription
    """
    patient = forms.ModelChoiceField(
        queryset=Appointment.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Prescription
        fields = ['patient', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }





class PrescriptionItemForm(forms.ModelForm):
    """
    Form for individual prescription items
    """
    disease = forms.ModelChoiceField(
        queryset=Disease.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    medicine = forms.ModelChoiceField(
        queryset=Medicine.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PrescriptionItem
        fields = ['disease', 'medicine', 'dosage', 'frequency', 'duration', 'instructions']
        widgets = {
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

# Create a formset for prescription items
PrescriptionItemFormSet = inlineformset_factory(
    Prescription,
    PrescriptionItem,
    form=PrescriptionItemForm,
    extra=3,  # Allow adding up to 3 items initially
    can_delete=True
)





# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['name','age','mobile','address']
#
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['name','mobile','specialization']


class PaymentOptionForm(forms.ModelForm):
    class Meta:
        model = PaymentOptions
        fields = ['email','f_name','l_name','address']