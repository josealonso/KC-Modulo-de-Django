# Generated by Django 2.0 on 2018-02-09 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0025_auto_20180208_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 22, 41, 32, 560006)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Título', max_length=130),
        ),
    ]
