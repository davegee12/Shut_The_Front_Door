# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-29 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0006_keyword_filter_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='genre_to_filter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
