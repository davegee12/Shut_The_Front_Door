# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-31 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0003_remove_user_query_data'),
        ('filter', '0010_auto_20190531_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='End_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_end_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keyword_associated_with_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyword_end_date', to='filter.Keyword')),
                ('user_associated_with_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filtering_user', to='login_reg.User')),
            ],
        ),
    ]
