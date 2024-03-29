# Generated by Django 4.2.6 on 2024-02-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0007_tvshow_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='acter',
            field=models.CharField(max_length=50, null=True, verbose_name='гл актер'),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='image2',
            field=models.ImageField(null=True, upload_to='cinema/', verbose_name='фон'),
        ),
        migrations.AddField(
            model_name='tvshow',
            name='otzv',
            field=models.CharField(max_length=50, null=True, verbose_name='otzzv'),
        ),
    ]
