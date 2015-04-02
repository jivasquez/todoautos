# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20150320_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
