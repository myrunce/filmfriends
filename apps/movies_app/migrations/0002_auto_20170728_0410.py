# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='movie',
        ),
        migrations.AddField(
            model_name='showtime',
            name='moveieID',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]