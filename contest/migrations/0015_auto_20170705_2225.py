# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-05 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20170705_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutioncode',
            name='problem_associated',
        ),
        migrations.RemoveField(
            model_name='solutioncode',
            name='user_associated',
        ),
        migrations.DeleteModel(
            name='SolutionCode',
        ),
    ]
