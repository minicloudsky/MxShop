# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-06 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200506_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 16, 50, 21, 599780), verbose_name='添加时间'),
        ),
    ]
