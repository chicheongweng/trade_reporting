# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-13 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180411_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_stamp',
            field=models.DateField(verbose_name='Time Stamp'),
        ),
    ]
