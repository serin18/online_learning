# Generated by Django 5.0.1 on 2024-06-13 07:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0022_admin_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_login',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
