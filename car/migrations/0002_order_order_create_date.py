# Generated by Django 5.1.4 on 2024-12-17 20:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]