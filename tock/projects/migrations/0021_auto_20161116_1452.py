# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_profitlossaccount_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profitlossaccount',
            name='account_type',
            field=models.CharField(choices=[('Revenue', 'Revenue'), ('Expense', 'Expense')], default='Revenue', max_length=200),
        ),
    ]
