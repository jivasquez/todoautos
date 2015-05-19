# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20150519_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='publication',
            field=models.ForeignKey(related_name='contact_numbers', to='main_app.Publication', null=True),
            preserve_default=True,
        ),
    ]
