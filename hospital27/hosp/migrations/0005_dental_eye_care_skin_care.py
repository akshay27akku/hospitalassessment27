# Generated by Django 5.1.3 on 2024-12-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0004_alter_bed_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eye_Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skin_Care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
