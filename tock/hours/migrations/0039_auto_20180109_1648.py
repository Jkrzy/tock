# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-09 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0038_deduplicate_tcos'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timecardobject',
            unique_together=set([('timecard', 'project')]),
        ),
    ]
