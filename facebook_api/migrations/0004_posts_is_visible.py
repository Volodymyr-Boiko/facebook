# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_api', '0003_auto_20170722_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
