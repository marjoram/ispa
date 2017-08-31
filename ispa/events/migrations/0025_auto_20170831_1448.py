# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-31 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_remove_event_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='allow_anonymous_rsvp',
            field=models.BooleanField(default=False, help_text='Even anonymous users can rsvp, without adding any info.', verbose_name='Allow anonymous RSVP'),
        ),
        migrations.AddField(
            model_name='event',
            name='available_seats',
            field=models.PositiveIntegerField(blank=True, help_text='Set this to a number if only a limited amount of slots are  available for this event. If you chose to display this on your site, you can create a sense of urgency for your users to RSVP before all slots are taken. As soon as all slots are taken, users cannot RSVP for this event any more.', null=True, verbose_name='Available seats'),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 1, 14, 48, 28, 336791, tzinfo=utc), verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='event',
            name='hide_available_seats',
            field=models.BooleanField(default=False, help_text='If you set the number of available seats you can check this field in order to hide that number from your users.', verbose_name='Hide available seat information'),
        ),
        migrations.AddField(
            model_name='event',
            name='max_guests',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 31, 14, 48, 28, 336721, tzinfo=utc), verbose_name='Start date'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]