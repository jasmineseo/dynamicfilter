# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicfilterapp', '0012_task_testfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='testfield',
        ),
    ]
