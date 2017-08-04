# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_eventtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[(8, 'event'), (5, 'semester'), (3, 'meeting')], max_length=128, null=True, verbose_name='Event Type'),
        ),
    ]
