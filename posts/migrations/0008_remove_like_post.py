# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 16:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170417_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
    ]