# Generated by Django 5.1.4 on 2024-12-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_order_order_order_status_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_user_contact',
            field=models.CharField(default='+', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='order_user_fio',
            field=models.CharField(default='+', max_length=20),
        ),
    ]
