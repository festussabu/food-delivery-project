# Generated by Django 5.0.1 on 2024-03-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0012_remove_pnrgenerator_id_alter_pnrgenerator_pnr_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoveTrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_station', models.CharField(choices=[('EKM', 'Ernakulam'), ('TRV', 'Trivandrum'), ('KLM', 'Kollam')], default='', max_length=240)),
            ],
        ),
    ]