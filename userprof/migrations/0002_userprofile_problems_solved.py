# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-03 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0010_problem_solved_by_whom'),
        ('userprof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='problems_solved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_who_solved', to='contest.Problem'),
        ),
    ]