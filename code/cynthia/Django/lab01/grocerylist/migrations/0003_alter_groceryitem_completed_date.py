# Generated by Django 4.2 on 2023-04-05 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0002_alter_groceryitem_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='completed date'),
        ),
    ]