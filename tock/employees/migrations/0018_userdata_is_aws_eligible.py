# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_auto_20161116_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='is_aws_eligible',
            field=models.BooleanField(default=False, verbose_name='Is alternative work schedule eligible'),
        ),
    ]
