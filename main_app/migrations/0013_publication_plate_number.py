# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20150515_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='plate_number',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
