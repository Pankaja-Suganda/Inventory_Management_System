# Generated by Django 2.2.10 on 2021-11-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0009_auto_20211126_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='status',
            field=models.IntegerField(choices=[(1, 'In Stock'), (0, 'Out Stock')], default=1),
        ),
    ]
