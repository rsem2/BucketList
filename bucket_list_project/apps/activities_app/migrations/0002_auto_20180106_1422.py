# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-06 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20180105_1407'),
        ('activities_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='people',
            field=models.ManyToManyField(related_name='activities', to='users_app.User'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_created', to='users_app.User'),
        ),
    ]
