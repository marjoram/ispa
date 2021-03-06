# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-31 20:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20170831_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvp', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 1, 20, 21, 34, 245862, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 20, 21, 34, 245759, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.UserProfile'),
        ),
    ]
