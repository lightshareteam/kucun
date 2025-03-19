# Generated by Django 4.2.6 on 2025-03-10 03:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_product_height_alter_product_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='low_stock_threshold',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='库存阈值'),
        ),
    ]
