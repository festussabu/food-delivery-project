# Generated by Django 5.0.1 on 2024-04-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0017_remove_customer_pnr_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pre_order',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]