# Generated by Django 3.1.4 on 2020-12-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_url_shortened_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(max_length=5000, verbose_name='Original Url'),
        ),
    ]
