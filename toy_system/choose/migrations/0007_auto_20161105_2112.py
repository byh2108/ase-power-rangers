# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choose', '0006_orderrecord_table_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderrecord',
            name='table_id',
        ),
        migrations.AddField(
            model_name='custrecord',
            name='table_id',
            field=models.IntegerField(default=0),
        ),
    ]
