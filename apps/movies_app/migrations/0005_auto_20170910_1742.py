# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0004_auto_20170910_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='user',
            field=models.ManyToManyField(related_name='users_attending', to='movies_app.User'),
        ),
    ]
