# Generated by Django 4.2 on 2023-04-07 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0004_click'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='click',
            name='use_count',
        ),
    ]
