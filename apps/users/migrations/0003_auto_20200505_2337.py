# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-05 15:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200505_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 23, 37, 49, 18272), verbose_name='添加时间'),
        ),
    ]
