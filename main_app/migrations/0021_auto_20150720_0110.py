# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20150720_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'publications'),
        ),
    ]
