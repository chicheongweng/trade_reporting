# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-16 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_centers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationcenter',
            name='name_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='operationcenter',
            name='name_zh_hans',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='operationcenter',
            name='name_zh_hant',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
