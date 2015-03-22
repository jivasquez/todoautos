# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publication_date', models.DateTimeField(verbose_name=b'date published')),
                ('type_of_vehicle', models.CharField(max_length=200)),
                ('vehicle_body', models.CharField(max_length=200)),
                ('fuel', models.CharField(max_length=200)),
                ('at_transmission', models.NullBooleanField()),
                ('air_conditioner', models.NullBooleanField()),
                ('first_owner', models.NullBooleanField()),
                ('centralized_locking', models.NullBooleanField()),
                ('airbag', models.NullBooleanField()),
                ('abs_break', models.NullBooleanField()),
                ('kilometers', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Marca',
            new_name='Brand',
        ),
        migrations.RemoveField(
            model_name='auto',
            name='marca',
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.AddField(
            model_name='publication',
            name='brand',
            field=models.ForeignKey(to='main_app.Brand'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='region',
            field=models.ForeignKey(to='main_app.Region'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(to='main_app.Region'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='nombre',
            new_name='name',
        ),
    ]
