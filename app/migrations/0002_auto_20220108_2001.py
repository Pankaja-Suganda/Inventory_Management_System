# Generated by Django 2.2.10 on 2022-01-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mobile_number',
            field=models.IntegerField(blank=True),
        ),
    ]
