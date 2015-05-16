# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20150513_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='version',
            new_name='model_version',
        ),
    ]
