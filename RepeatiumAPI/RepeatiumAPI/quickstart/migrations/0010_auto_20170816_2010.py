# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_auto_20170816_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='y',
        ),
        migrations.AddField(
            model_name='plan',
            name='isYearly',
            field=models.NullBooleanField(),
        ),
    ]
