# Generated by Django 4.2 on 2023-04-25 19:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_check_in_date_book_check_out_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='check_in_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]