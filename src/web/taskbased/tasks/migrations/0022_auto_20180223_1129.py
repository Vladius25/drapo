# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-23 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20170413_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='is_plagiarized',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]