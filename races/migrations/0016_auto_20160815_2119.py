# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0015_auto_20160811_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
