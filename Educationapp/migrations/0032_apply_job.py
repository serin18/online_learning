# Generated by Django 5.0.1 on 2024-06-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educationapp', '0031_alter_class_link_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
