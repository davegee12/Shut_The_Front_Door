# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-30 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_user_query_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='query_data',
        ),
    ]