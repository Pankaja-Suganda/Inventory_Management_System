# Generated by Django 2.2.10 on 2021-11-19 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20211119_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_material',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Product'),
        ),
    ]
