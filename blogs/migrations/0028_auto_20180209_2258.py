# Generated by Django 2.0 on 2018-02-09 22:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0027_auto_20180209_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Cuerpo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 9, 22, 58, 43, 246868), verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Vídeo'),
        ),
    ]
