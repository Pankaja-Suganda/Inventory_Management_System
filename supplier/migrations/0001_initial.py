# Generated by Django 2.2.10 on 2021-09-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('company', models.CharField(blank=True, max_length=150, verbose_name='company')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='name')),
                ('supplier_img', models.ImageField(blank=True, default='core/static/assets/images/supplier/default.png', null=True, upload_to='core/static/assets/images/supplier')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('mobile_number', models.IntegerField(blank=True, max_length=10)),
                ('fax_number', models.IntegerField(blank=True, max_length=10)),
                ('Address_1', models.CharField(max_length=250, verbose_name='postal address 1')),
                ('Address_2', models.CharField(max_length=250, verbose_name='postal address 2')),
                ('city', models.CharField(max_length=250, verbose_name='postal city')),
                ('joined_date', models.DateTimeField(auto_now=True)),
                ('po_count', models.IntegerField(default=0)),
                ('last_order_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
