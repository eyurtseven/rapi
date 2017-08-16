# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.TextField()),
                ('dayDuration', models.IntegerField()),
                ('dayDurationText', models.IntegerField()),
                ('projectCount', models.IntegerField()),
                ('projectCountText', models.TextField()),
                ('deviceCount', models.IntegerField()),
                ('deviceCountText', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('priceText', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
