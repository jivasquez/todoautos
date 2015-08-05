# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20150720_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationimage',
            name='source_url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
