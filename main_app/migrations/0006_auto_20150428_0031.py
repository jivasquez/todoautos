# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_publication_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
