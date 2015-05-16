# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20150428_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_new',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='year',
            field=models.IntegerField(default=2000),
            preserve_default=True,
        ),
    ]
