# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-03 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0001_initial'),
        ('contest', '0009_auto_20170630_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='solved_by_whom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='problem_solved_by', to='userprof.UserProfile'),
        ),
    ]
