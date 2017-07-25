# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-05 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0015_auto_20170705_2225'),
        ('userprof', '0004_remove_userprofile_problems_solved'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionCode',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('code_text', models.FileField(null=True, upload_to=b'')),
                ('problem_associated', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE,
                                                         related_name='solutions_to_problem', to='contest.Problem')),
                ('user_associated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                                      related_name='user_so', to='userprof.UserProfile')),
            ],
        ),
    ]
