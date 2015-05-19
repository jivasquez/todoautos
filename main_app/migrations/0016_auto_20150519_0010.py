# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20150516_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='publication',
            field=models.ForeignKey(related_name='contact_numbers', default=0, to='main_app.Publication'),
            preserve_default=False,
        ),
    ]
