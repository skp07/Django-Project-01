# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movieinfo_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='summary',
            field=models.CharField(default='No description found', max_length=2000),
        ),
    ]
