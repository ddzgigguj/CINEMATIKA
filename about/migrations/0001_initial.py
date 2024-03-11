# Generated by Django 4.2.6 on 2024-02-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]