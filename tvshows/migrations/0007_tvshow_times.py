# Generated by Django 4.2.6 on 2024-02-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0006_remove_tvshow_tr_tvshow_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='times',
            field=models.TimeField(null=True, verbose_name='время показа'),
        ),
    ]
