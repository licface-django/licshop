# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 03:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('home', '0003_my_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_user',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='my_user',
        ),
    ]
