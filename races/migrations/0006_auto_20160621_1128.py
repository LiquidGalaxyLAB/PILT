# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0005_auto_20160620_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='raceparticipant',
        ),
        migrations.AddField(
            model_name='position',
            name='raceparticipant',
            field=models.ForeignKey(default=27, on_delete=django.db.models.deletion.CASCADE, to='races.RaceParticipant'),
        ),
    ]
