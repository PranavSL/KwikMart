# Generated by Django 4.0.3 on 2022-04-03 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
    ]
