# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-05 16:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200505_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 6, 0, 3, 12, 423455), verbose_name='添加时间'),
        ),
    ]
