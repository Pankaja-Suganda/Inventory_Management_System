# Generated by Django 2.2.10 on 2021-11-19 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0008_auto_20211102_1537'),
        ('stock', '0002_product_material_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('material_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.Materials')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='material_ids',
            field=models.ManyToManyField(blank=True, null=True, to='stock.Product_Material'),
        ),
        migrations.AddField(
            model_name='product_material',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Product'),
        ),
    ]
