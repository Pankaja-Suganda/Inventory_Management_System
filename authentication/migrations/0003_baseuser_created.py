# Generated by Django 2.2.10 on 2021-08-22 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210823_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
