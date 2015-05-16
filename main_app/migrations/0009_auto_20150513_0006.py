# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20150430_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='motor_size',
        ),
        migrations.AddField(
            model_name='publication',
            name='alarm',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='assisted_steering',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='catalitic',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='doors',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='electric_mirrors',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='engine',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='model',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='version',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
