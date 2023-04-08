# Generated by Django 4.2 on 2023-04-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0003_alter_groceryitem_completed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='purchased_item',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(null=True, verbose_name='completed date'),
        ),
    ]
