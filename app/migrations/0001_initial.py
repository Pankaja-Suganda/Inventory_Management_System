# Generated by Django 2.2.10 on 2021-11-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(blank=True, max_length=150, verbose_name='company')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('mobile_number', models.IntegerField(blank=True, max_length=10)),
                ('Postal_Address_1', models.CharField(max_length=250, verbose_name='postal address 1')),
                ('Postal_Address_2', models.CharField(max_length=250, verbose_name='postal address 2')),
                ('Postal_city', models.CharField(max_length=250, verbose_name='postal city')),
                ('billing_Address_1', models.CharField(max_length=250, verbose_name='billing address 1')),
                ('billing_Address_2', models.CharField(max_length=250, verbose_name='billing address 2')),
                ('billing_city', models.CharField(max_length=250, verbose_name='billing city')),
            ],
        ),
    ]