# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheatreDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenName', models.CharField(max_length=25)),
                ('rowNumber', models.CharField(max_length=2)),
                ('maxCapacity', models.IntegerField()),
                ('aisleSeats', models.TextField()),
            ],
        ),
    ]
