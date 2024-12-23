from django.urls import path
from .import views
from .views import CustomLoginView, BillingInvoiceListView, overdue_invoices, BillingInvoiceDetailView, create_invoice, \
    AddPaymentView

urlpatterns = [

    path('',views.index,name="index"),
    path('blog/',views.blog,name="blog"),
    path('department/',views.department,name="department"),
    path('doctors/',views.doctors,name="doctors"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('appointment/',views.appointment_view,name="appointment"),
    path('success/',views.success,name="success"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('register/',views.register,name="register"),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('doctor_dashboard/',views.doctor_dashboard,name="doctor_dashboard"),
    path('error/',views.doctor_dashboard,name="error"),
    path('staff_dashboard/',views.staff_dashboard_view,name="staff_dashboard"),
    # path('appointment_list/',views.appointment_list,name="appointment_list"),
    path('apply_for_bed/', views.apply_for_bed, name='apply_for_bed'),
    path('eye_care/', views.eye_care_view, name='eye_care'),
    path('eye_care_template/',views.eye_care_template,name="eye_care_template"),
    path('dental/', views.dental_view, name='dental'),
    path('dental_template/',views.dental_template,name="dental_template"),
    path('skin_care/', views.skin_care_view, name='skin_care'),
    path('skin_care_template/',views.skin_care_template,name="skin_care_template"),
    path('physical_therappy_template/',views.physical_therappy_template,name="physical_therappy_template"),
    path('physical_therappy/',views.physical_therappy_view,name="physical_therappy"),
    path('diagnostic/',views.diagnostic_view,name="diagnostic"),
    path('surgery_service/',views.surgery_service_view,name="surgery_service"),
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    # path('appointment/<int:appointment_id>/update/',views.update_appointment_status, name='update_appointment_status'),
    path('appointment/<int:appointment_id>/update-status/',views.update_appointment_status,name='update_appointment_status'),
    path('prescription/create/',views.create_prescription,name='create_prescription'),
    path('prescription/<int:pk>/',views.prescription_detail,name='prescription_detail'),
    path('patient/prescriptions/',views.patient_prescriptions,name='patient_prescriptions'),
    path('doctor/prescriptions/', views.doctor_prescriptions, name='doctor_prescriptions'),
    path('invoices/',
         BillingInvoiceListView.as_view(),
         name='invoice-list'),

    # Invoice Detail View
    path('invoices/<int:pk>/',
         BillingInvoiceDetailView.as_view(),
         name='invoice-detail'),

    # Create New Invoice
    path('invoices/create/',
         create_invoice,
         name='create_invoice'),

    # Add Payment to Invoice
    path('invoices/<int:invoice_id>/add-payment/',
         AddPaymentView.as_view(),
         name='add-payment'),

    # Overdue Invoices
    path('invoices/overdue/',
         overdue_invoices,
         name='overdue-invoices'),

    # Print Invoice (optional)
    path('invoices/<int:pk>/print/',
         BillingInvoiceDetailView.as_view(template_name='billing/invoice_print.html'),
         name='print-invoice'),



]