# Generated by Django 5.1.3 on 2024-12-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0021_alter_appointment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
