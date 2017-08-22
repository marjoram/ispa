# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-20 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_userprofile_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dues_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SM', 'Sophmore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=56),
        ),
    ]
