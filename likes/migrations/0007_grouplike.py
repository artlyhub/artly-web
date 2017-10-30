# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profileimage_status_main'),
        ('groups', '0001_initial'),
        ('likes', '0006_profileimagelike'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='groups.Group')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_likes', to='accounts.Profile')),
            ],
        ),
    ]