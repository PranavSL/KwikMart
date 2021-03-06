# Generated by Django 4.0.3 on 2022-04-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_order_address_remove_order_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsOfUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
            ],
        ),
    ]
