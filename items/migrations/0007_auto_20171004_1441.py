# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-04 14:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20171004_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[''], size=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[''], size=None),
        ),
    ]
