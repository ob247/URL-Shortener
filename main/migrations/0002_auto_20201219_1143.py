# Generated by Django 3.1.4 on 2020-12-19 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Original Url')),
                ('shortened_url', models.URLField(blank=True, null=True, verbose_name='Shortened Url')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
