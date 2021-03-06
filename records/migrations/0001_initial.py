# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-24 22:20
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_image_status_main'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_number', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('artist', models.CharField(max_length=50)),
                ('purchased_price', models.BigIntegerField()),
                ('message', models.TextField(default='')),
                ('for_sale', models.BooleanField(default=1)),
                ('sale_method', models.CharField(choices=[('Sale', 'Regular Sale'), ('Fund', 'Crowd Art Fund'), ('Auction', 'Auction')], default='Sale', max_length=7)),
                ('sale_price', models.BigIntegerField()),
                ('auction_price_history', django.contrib.postgres.fields.jsonb.JSONField(default='{}')),
                ('private_info', models.BooleanField(default=0)),
                ('artly_possession', models.BooleanField(default=0)),
                ('previous_hash', models.CharField(default='', max_length=64)),
                ('current_hash', models.CharField(default='', max_length=64)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='items.Item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
