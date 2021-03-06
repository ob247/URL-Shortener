# Generated by Django 3.1.4 on 2020-12-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_urls_url_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(verbose_name='Original Url')),
                ('shortened_url', models.URLField(verbose_name='Shortened Url')),
                ('url_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Url Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
