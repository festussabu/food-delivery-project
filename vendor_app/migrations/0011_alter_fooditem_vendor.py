# Generated by Django 5.0.2 on 2024-02-19 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0010_alter_fooditem_food_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_app.vendor'),
        ),
    ]