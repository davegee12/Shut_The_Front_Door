# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-30 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0007_auto_20190529_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='query_data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
