# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-07 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNo', models.IntegerField(blank=True, default='', max_length=100)),
                ('branch', models.TextField()),
                ('accountType', models.TextField()),
            ],
        ),
    ]
