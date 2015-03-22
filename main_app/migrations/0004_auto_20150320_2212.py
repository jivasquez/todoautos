# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20150320_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='city',
            field=models.ForeignKey(to='main_app.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='kilometers',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='region',
            field=models.ForeignKey(to='main_app.Region', null=True),
            preserve_default=True,
        ),
    ]
