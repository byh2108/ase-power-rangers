# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choose', '0010_auto_20161114_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='categories',
            field=models.CharField(choices=[(b'AP', b'Appetizer'), (b'MC', b'Main Course'), (b'DE', b'Dessert'), (b'BE', b'Beverage')], default=b'Appetizer', max_length=20),
        ),
    ]