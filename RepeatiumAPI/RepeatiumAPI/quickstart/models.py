# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Package(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
