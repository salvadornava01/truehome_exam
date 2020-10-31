# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-30 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20201030_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='property_id',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='activity_id',
            new_name='activity',
        ),
        migrations.AlterField(
            model_name='property',
            name='disabled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
