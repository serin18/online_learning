# Generated by Django 5.0.1 on 2024-06-09 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0010_user_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_log',
            name='password',
            field=models.CharField(default='pending', max_length=25),
        ),
    ]
