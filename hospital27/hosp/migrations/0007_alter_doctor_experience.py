# Generated by Django 5.1.3 on 2024-12-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0006_doctor_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.CharField(max_length=15),
        ),
    ]
