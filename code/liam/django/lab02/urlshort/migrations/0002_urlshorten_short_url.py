# Generated by Django 4.2 on 2023-04-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshorten',
            name='short_url',
            field=models.CharField(default='TESTID', max_length=6, verbose_name='short url'),
        ),
    ]
