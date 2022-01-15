# Generated by Django 2.2.10 on 2021-10-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0004_auto_20211030_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cmaterial',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
