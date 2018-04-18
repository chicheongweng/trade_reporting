# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 08:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0003_auto_20180418_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profit',
            options={'verbose_name': 'profit', 'verbose_name_plural': 'profit'},
        ),
        migrations.AlterField(
            model_name='profit',
            name='net',
            field=models.FloatField(verbose_name='net'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='symbol',
            field=models.CharField(max_length=16, verbose_name='symbol'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
