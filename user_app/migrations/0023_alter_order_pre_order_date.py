# Generated by Django 5.0.1 on 2024-04-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0022_delete_preorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pre_order_date',
            field=models.CharField(blank=True, default='NA', max_length=200, null=True),
        ),
    ]
