# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizePaper', '0003_auto_20170723_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
