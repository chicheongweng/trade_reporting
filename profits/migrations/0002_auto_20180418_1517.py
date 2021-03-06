# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 07:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit',
            name='net',
            field=models.FloatField(verbose_name='\u5229\u6f64'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='symbol',
            field=models.CharField(max_length=16, verbose_name='\u7b26\u865f'),
        ),
        migrations.AlterField(
            model_name='profit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6236'),
        ),
    ]
