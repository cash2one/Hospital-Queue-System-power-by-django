# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot')),
                ('privacy', models.CharField(choices=[('open', 'Open'), ('registered', 'Registered'), ('closed', 'Closed')], default='registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, '男性'), (2, '女性')], null=True, verbose_name='性别')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth date')),
                ('identifyid', models.CharField(max_length=18, null=True, verbose_name='身份证号')),
                ('phonenumber', models.CharField(max_length=11, null=True, verbose_name='手机号')),
                ('about_me', models.TextField(blank=True, verbose_name='about me')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='患者管理', to=settings.AUTH_USER_MODEL, verbose_name='患者')),
            ],
            options={
                'permissions': (('view_profile', 'Can view profile'),),
                'abstract': False,
            },
        ),
    ]
