# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicfilterapp', '0059_auto_20160725_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]