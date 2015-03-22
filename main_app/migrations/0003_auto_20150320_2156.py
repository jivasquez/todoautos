# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20150320_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='fuel',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='kilometers',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='type_of_vehicle',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publication',
            name='vehicle_body',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
