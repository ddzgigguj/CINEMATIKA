# Generated by Django 4.2.6 on 2024-02-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0005_remove_tvshow_image1_remove_tvshow_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='tr',
        ),
        migrations.AddField(
            model_name='tvshow',
            name='trailer',
            field=models.URLField(blank=True, verbose_name='Укажите трейлер'),
        ),
    ]
