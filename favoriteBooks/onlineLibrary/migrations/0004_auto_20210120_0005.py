# Generated by Django 2.2.4 on 2021-01-20 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineLibrary', '0003_auto_20210120_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favoriteBooks',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
