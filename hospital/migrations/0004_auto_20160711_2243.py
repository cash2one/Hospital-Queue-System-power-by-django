# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20160707_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_note',
            name='time',
            field=models.DateField(verbose_name='日期'),
        ),
    ]