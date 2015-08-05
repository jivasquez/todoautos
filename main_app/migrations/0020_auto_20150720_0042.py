# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_publicationimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationimage',
            name='image',
            field=models.ImageField(upload_to=b'publications'),
        ),
    ]
