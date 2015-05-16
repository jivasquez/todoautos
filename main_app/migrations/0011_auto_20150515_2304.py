# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20150514_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='chileautos_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='source',
            field=models.CharField(default='todoautos', max_length=200),
            preserve_default=False,
        ),
    ]
