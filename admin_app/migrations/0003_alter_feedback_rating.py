# Generated by Django 5.0.2 on 2024-03-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
