# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-31 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_auto_20201030_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='activity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='activities.Activity'),
        ),
    ]
