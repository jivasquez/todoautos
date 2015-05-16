# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20150428_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='color',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='motor_size',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
