# Generated by Django 4.2 on 2023-04-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images', verbose_name='image'),
            preserve_default=False,
        ),
    ]
