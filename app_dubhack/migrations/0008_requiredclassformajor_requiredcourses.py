# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_dubhack', '0007_auto_20161016_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequiredClassForMajor',
            fields=[
                ('requiredID', models.AutoField(primary_key=True, serialize=False)),
                ('majorname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requiredCourseName', models.CharField(max_length=50)),
                ('requiredCourseNumber', models.IntegerField()),
                ('requiredID', models.ForeignKey(db_column='requiredID', on_delete=django.db.models.deletion.DO_NOTHING, to='app_dubhack.RequiredClassForMajor')),
            ],
        ),
    ]
