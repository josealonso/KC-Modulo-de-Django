# Generated by Django 2.0 on 2018-01-03 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180103_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='posts',
        ),
    ]