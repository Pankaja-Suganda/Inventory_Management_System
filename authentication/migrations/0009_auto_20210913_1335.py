# Generated by Django 2.2.10 on 2021-09-13 08:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210913_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, region=None),
        ),
    ]
