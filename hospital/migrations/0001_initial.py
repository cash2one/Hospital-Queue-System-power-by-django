# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('workid', models.CharField(max_length=10, verbose_name='工号')),
                ('department', models.CharField(max_length=11, verbose_name='科室')),
                ('phonenumber', models.CharField(max_length=11, verbose_name='手机号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '医生',
                'verbose_name_plural': '医生管理',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200, verbose_name='标题')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.CharField(max_length=5000, verbose_name='内容')),
                ('time', models.DateField(auto_now_add=True, verbose_name='日期')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻管理',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('gender', models.BooleanField(default=True, verbose_name='性别')),
                ('identifyid', models.CharField(max_length=18, verbose_name='身份证号')),
                ('phonenumber', models.CharField(max_length=11, verbose_name='手机号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '患者',
                'verbose_name_plural': '患者管理',
            },
        ),
        migrations.CreateModel(
            name='register_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.BooleanField(default=False, verbose_name='完成挂诊')),
                ('time', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
            options={
                'verbose_name': '挂诊',
                'verbose_name_plural': '挂诊管理',
            },
        ),
    ]
