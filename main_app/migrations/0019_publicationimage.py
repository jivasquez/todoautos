# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20150610_0310'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=350, width_field=400, upload_to=b'publications')),
                ('publication', models.ForeignKey(related_name='publication_images', to='main_app.Publication', null=True)),
            ],
        ),
    ]
