# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_foodtypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtypes',
            name='childtypenames',
            field=models.CharField(max_length=256),
        ),
    ]