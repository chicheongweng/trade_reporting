# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_centers', '0005_auto_20180418_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operationcenter',
            options={'verbose_name': '\u71df\u904b\u4e2d\u5fc3', 'verbose_name_plural': 'operation centers'},
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='name',
            field=models.CharField(max_length=64, verbose_name='\u4e2d\u5fc3\u540d\u7a31'),
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='name_en',
            field=models.CharField(max_length=64, null=True, verbose_name='\u4e2d\u5fc3\u540d\u7a31'),
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='name_zh_hans',
            field=models.CharField(max_length=64, null=True, verbose_name='\u4e2d\u5fc3\u540d\u7a31'),
        ),
        migrations.AlterField(
            model_name='operationcenter',
            name='name_zh_hant',
            field=models.CharField(max_length=64, null=True, verbose_name='\u4e2d\u5fc3\u540d\u7a31'),
        ),
    ]
