# Generated by Django 4.2.16 on 2024-12-07 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='zipcode',
            new_name='pincode',
        ),
    ]
