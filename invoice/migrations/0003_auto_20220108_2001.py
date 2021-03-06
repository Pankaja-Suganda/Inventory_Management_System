# Generated by Django 2.2.10 on 2022-01-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20211124_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='issued_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='product_ids',
            field=models.ManyToManyField(blank=True, to='invoice.Invoice_Product'),
        ),
    ]
