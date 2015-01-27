# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_auto_20150126_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 23, 45, 13, 421055), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(unique=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(unique=True, max_length=256),
            preserve_default=True,
        ),
    ]
