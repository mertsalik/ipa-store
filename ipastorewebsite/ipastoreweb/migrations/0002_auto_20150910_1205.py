# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipastoreweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipa',
            name='download_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'Download Count'),
        ),
        migrations.AlterField(
            model_name='ipa',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Published'),
        ),
    ]
