# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_app', '0010_auto_20170118_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField(default=0, verbose_name='Position')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('name_en', models.CharField(blank=True, help_text='Name in english', max_length=140, null=True, verbose_name='Name in english')),
                ('content_en', models.TextField(blank=True, help_text='use HTML for better result', null=True, verbose_name='Content in english')),
                ('name_ru', models.CharField(blank=True, help_text='Name in russian', max_length=140, null=True, verbose_name='Name in russian')),
                ('content_ru', models.TextField(blank=True, help_text='use HTML for better result', null=True, verbose_name='Content in russian')),
            ],
            options={
                'ordering': ['pos'],
                'verbose_name_plural': 'Programmes',
                'verbose_name': 'Programm',
            },
        ),
    ]
