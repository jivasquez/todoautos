# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20150519_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='chileautos_id',
            field=models.IntegerField(unique=True, null=True),
        ),
    ]
