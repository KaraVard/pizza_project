# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0002_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]