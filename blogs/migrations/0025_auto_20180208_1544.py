# Generated by Django 2.0 on 2018-02-08 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0024_auto_20180115_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 15, 44, 35, 808358)),
        ),
    ]
