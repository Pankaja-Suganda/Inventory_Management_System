# Generated by Django 2.2.10 on 2021-11-15 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cproduct',
            old_name='po_id',
            new_name='so_id',
        ),
    ]
