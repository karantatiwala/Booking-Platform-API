# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TheatreDetails(models.Model):
	screenName = models.CharField(max_length=25)
	rowNumber = models.CharField(max_length=2)
	maxCapacity = models.IntegerField()
	bookedSeats = models.TextField(null=True)
