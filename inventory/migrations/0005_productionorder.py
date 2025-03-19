# Generated by Django 4.2.6 on 2025-03-11 08:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_product_low_stock_threshold'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100, verbose_name='订单号')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='订单数量')),
                ('remaining_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='剩余数量')),
                ('status', models.CharField(choices=[('生产中', '生产中'), ('部分完成', '部分完成'), ('已完成', '已完成')], default='生产中', max_length=20, verbose_name='状态')),
                ('notes', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '生产订单',
                'verbose_name_plural': '生产订单',
                'ordering': ['-created_at'],
            },
        ),
    ]
