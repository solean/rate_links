# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 22, 52, 28, 5996), auto_now_add=True),
            preserve_default=True,
        ),
    ]
