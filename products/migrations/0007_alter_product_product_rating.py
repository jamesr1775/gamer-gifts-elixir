# Generated by Django 3.2.9 on 2021-12-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211209_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]
