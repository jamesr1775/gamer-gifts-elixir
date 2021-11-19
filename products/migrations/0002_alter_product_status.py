# Generated by Django 3.2.9 on 2021-11-17 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Low Stock', 'Lowstock'), ('In Stock', 'Instock'), ('Out of Stock', 'Outofstock')], default='In Stock', max_length=254),
        ),
    ]