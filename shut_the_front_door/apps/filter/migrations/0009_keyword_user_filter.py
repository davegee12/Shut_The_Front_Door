# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-31 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_remove_user_query_data'),
        ('filter', '0008_keyword_query_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='user_filter',
            field=models.ManyToManyField(related_name='user_filter', to='login_reg.User'),
        ),
    ]
