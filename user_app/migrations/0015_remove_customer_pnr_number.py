# Generated by Django 5.0.1 on 2024-03-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0014_delete_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='pnr_number',
        ),
    ]