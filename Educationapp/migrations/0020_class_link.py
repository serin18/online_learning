# Generated by Django 5.0.1 on 2024-06-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0019_flutter_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=25)),
                ('time', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=25)),
                ('link', models.CharField(max_length=25)),
            ],
        ),
    ]
