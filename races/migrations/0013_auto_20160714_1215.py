# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0012_auto_20160713_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='imageURL',
            field=models.CharField(max_length=300),
        ),
    ]