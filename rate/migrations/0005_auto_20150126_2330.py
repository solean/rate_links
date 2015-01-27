# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_auto_20150126_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 23, 30, 32, 499228), auto_now_add=True),
            preserve_default=True,
        ),
    ]
