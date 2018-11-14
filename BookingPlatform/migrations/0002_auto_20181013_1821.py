# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingPlatform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatredetails',
            name='aisleSeats',
        ),
        migrations.AddField(
            model_name='theatredetails',
            name='bookedSeats',
            field=models.TextField(null=True),
        ),
    ]
