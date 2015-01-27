# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_auto_20150126_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='num_ratings',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='avg_rating',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 23, 29, 2, 90245), auto_now_add=True),
            preserve_default=True,
        ),
    ]
