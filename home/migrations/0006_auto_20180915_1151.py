# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-15 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180915_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teaminfo',
            name='info',
            field=models.CharField(max_length=500),
        ),
    ]
