# Generated by Django 5.0.1 on 2024-06-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0017_trial_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='date',
            field=models.CharField(max_length=25),
        ),
    ]
