# Generated by Django 4.2 on 2023-04-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_urlshorten_short_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshorten',
            name='last_user',
            field=models.CharField(default='nobody', max_length=30, verbose_name='last user to redirect'),
        ),
    ]
