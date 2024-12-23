# Generated by Django 5.1.3 on 2024-11-24 07:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.CharField(choices=[('akshay', 'Akshay'), ('abhijith', 'Abhijith'), ('arjun', 'Arjun'), ('akhil', 'Akhil')], max_length=20)),
                ('department', models.CharField(choices=[('neurologist', 'Neurologist'), ('cardiologist', 'Cardiologist'), ('ortho', 'Ortho'), ('thyroid', 'Thyroid')], max_length=20)),
                ('name', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')])),
            ],
        ),
    ]
