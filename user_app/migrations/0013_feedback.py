# Generated by Django 5.0.2 on 2024-03-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_alter_order_customer_name_alter_order_train_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_feedback', models.CharField(max_length=200)),
            ],
        ),
    ]
