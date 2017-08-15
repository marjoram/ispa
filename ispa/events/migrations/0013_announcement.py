# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-13 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20170813_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True, unique=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
