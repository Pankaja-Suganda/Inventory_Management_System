# Generated by Django 2.2.10 on 2021-11-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0007_auto_20211019_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='quatity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
