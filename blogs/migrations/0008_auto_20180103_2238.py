# Generated by Django 2.0 on 2018-01-03 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20180103_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_name',
            new_name='title',
        ),
    ]
