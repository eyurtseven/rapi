# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20170816_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='isYearlyPlan',
            field=models.BooleanField(default=True),
        ),
    ]