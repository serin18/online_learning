# Generated by Django 5.0.1 on 2024-06-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0003_remove_course_register_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_register',
            name='course',
            field=models.CharField(default='pending', max_length=25),
        ),
    ]
