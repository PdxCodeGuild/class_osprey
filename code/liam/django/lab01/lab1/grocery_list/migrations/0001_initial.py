# Generated by Django 4.2 on 2023-04-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_description', models.CharField(max_length=40)),
                ('create_date', models.DateField(verbose_name='date added')),
                ('complete_date', models.DateField(auto_now_add=True, verbose_name='date completed')),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]