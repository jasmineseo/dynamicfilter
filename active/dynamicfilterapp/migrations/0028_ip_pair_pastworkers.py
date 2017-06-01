# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicfilterapp', '0027_auto_20160610_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_pair',
            name='pastWorkers',
            field=models.ManyToManyField(related_name='ip_pairs_completed', to='dynamicfilterapp.WorkerID'),
        ),
    ]
