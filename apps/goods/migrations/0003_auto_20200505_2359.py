# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-05-05 15:59
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200505_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]