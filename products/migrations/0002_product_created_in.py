# Generated by Django 4.1.7 on 2023-08-23 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]