# Generated by Django 4.1.5 on 2024-11-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Pooja Samgri'), ('H', 'Havan Samagri'), ('S', 'Spices'), ('J', 'Jadi Booti'), ('JM', 'Jap Mala')], max_length=2, null=True),
        ),
    ]
