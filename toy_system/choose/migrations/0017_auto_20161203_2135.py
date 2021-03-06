# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-03 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('choose', '0016_merge_20161203_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecord',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='menuimage',
            name='photo',
            field=models.ImageField(upload_to=b'menu/'),
        ),
    ]
