# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-05 15:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 23, 34, 26, 856130), verbose_name='添加时间'),
        ),
    ]
