# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_auto_20170728_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='time',
            field=models.CharField(max_length=255),
        ),
    ]
