# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-30 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='query_data',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
