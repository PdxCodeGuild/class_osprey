# Generated by Django 4.2 on 2023-04-07 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0004_groceryitem_purchased_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groceryitem',
            old_name='purchased_item',
            new_name='is_completed',
        ),
    ]
