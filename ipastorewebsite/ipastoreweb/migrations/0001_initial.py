# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ipa',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'Identifier', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('app_version', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('download_count', models.IntegerField(verbose_name=b'Download Count')),
                ('file_path', models.CharField(max_length=500)),
            ],
        ),
    ]
