# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
