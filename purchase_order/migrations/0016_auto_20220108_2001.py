# Generated by Django 2.2.10 on 2022-01-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0015_auto_20211119_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='tax_rate',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='material_ids',
            field=models.ManyToManyField(blank=True, to='purchase_order.CMaterial'),
        ),
    ]
