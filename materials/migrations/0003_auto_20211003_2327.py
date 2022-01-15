# Generated by Django 2.2.10 on 2021-10-03 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_materials_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='quatity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materials',
            name='status',
            field=models.IntegerField(choices=[(0, 'In Stock'), (1, 'Out Stock')], default=0),
        ),
    ]
