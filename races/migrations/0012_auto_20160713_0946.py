# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0011_auto_20160713_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitiontaskparticipantposition',
            old_name='raceparticipant',
            new_name='taskparticipant',
        ),
    ]