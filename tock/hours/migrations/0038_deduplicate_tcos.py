# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-09 21:50
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, schema_editor):
    Timecard = apps.get_model('hours', 'Timecard')
    for tc in Timecard.objects.all():
        tcos = tc.timecardobjects.all()
        for tco in tcos:
            duplicates = tcos.filter(project=tco.project)
            if duplicates.count() > 1:
                total_hours = duplicates[0].hours_spent
                for d in duplicates[1:]:
                    total_hours += d.hours_spent
                    d.delete()
                duplicates[0].hours_spent = total_hours
                duplicates[0].save()

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20171229_1156'),
        ('hours', '0037_remove_timecardprefilldata_user'),
    ]

    operations = [migrations.RunPython(forward)
    ]
