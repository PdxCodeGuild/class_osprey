# Generated by Django 4.2 on 2023-04-07 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_conversion_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversion',
            name='created_date',
        ),
    ]
