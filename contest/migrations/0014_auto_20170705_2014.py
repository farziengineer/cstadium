# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-05 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0013_solutioncode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutioncode',
            name='code_text',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
