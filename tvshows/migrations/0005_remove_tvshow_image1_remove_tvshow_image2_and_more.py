# Generated by Django 4.2.6 on 2024-02-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0004_tvshow_image2_tvshow_image3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='trailer',
        ),
        migrations.AddField(
            model_name='tvshow',
            name='tr',
            field=models.FileField(null=True, upload_to='vid/'),
        ),
    ]
