# Generated by Django 2.0 on 2018-01-15 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0023_auto_20180115_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 12, 30, 14, 229258)),
        ),
    ]
