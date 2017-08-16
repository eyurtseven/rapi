# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Package(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Plan(models.Model):
    planName = models.TextField()
    projectCount = models.IntegerField()
    projectCountText = models.TextField()
    deviceCount = models.IntegerField()
    deviceCountText = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    priceText = models.TextField()
    isYearly = models.TextField(default='False')
    description = models.TextField()
