# Generated by Django 5.1.4 on 2024-12-17 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_order_order_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='body_id',
        ),
        migrations.RemoveField(
            model_name='car',
            name='prod_year',
        ),
        migrations.AddField(
            model_name='car',
            name='car_body_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='car.body'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_prod_year',
            field=models.IntegerField(default=2000),
        ),
    ]
