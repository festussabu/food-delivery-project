# Generated by Django 5.0.1 on 2024-03-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0015_delete_movetrain'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoveTrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_station', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
