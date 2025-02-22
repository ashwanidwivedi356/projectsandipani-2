# Generated by Django 4.2.16 on 2024-12-07 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_rename_zipcode_booking_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pandit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('specialty', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(default='Unknown', max_length=50)),
                ('state', models.CharField(default='Unknown', max_length=50)),
                ('availability', models.BooleanField(default=True)),
                ('contact_number', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
