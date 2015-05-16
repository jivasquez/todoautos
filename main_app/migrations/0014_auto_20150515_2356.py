# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_publication_plate_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=30)),
                ('phone_type', models.CharField(max_length=30)),
                ('publication', models.ForeignKey(related_name='contact_numbers', to='main_app.Publication')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publication',
            name='contact_name',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
