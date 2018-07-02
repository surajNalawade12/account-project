# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='owner',
        ),
        migrations.AddField(
            model_name='employee',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account'),
        ),
    ]