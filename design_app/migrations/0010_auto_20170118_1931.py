# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_app', '0009_auto_20170118_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='programm',
            name='short_en',
            field=models.TextField(blank=True, help_text='140 symbols', null=True, verbose_name='Short in english'),
        ),
        migrations.AddField(
            model_name='programm',
            name='short_ru',
            field=models.TextField(blank=True, help_text='140 symbols', null=True, verbose_name='Short in russian'),
        ),
    ]
