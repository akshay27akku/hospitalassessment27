# Generated by Django 5.1.3 on 2024-12-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0024_alter_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
