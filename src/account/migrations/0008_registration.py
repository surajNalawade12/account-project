# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('confirmPassword', models.TextField()),
            ],
        ),
    ]
