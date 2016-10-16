# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dubhack', '0002_auto_20161016_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorRequirements',
            fields=[
                ('majorid', models.AutoField(db_column='MajorRequirements', primary_key=True, serialize=False)),
                ('majorname', models.CharField(db_column='MajorRequirementsName', max_length=50)),
            ],
            options={
                'db_table': 'MAJOR_REQUIREMENTS',
            },
        ),
    ]
