# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171127_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('static_url', models.URLField()),
                ('media_url', models.URLField()),
            ],
            options={
                'db_table': 'config',
            },
        ),
        #  migrations.RenameField(
            #  model_name='singup',
            #  old_name='user_id',
            #  new_name='user',
        #  ),
        migrations.AlterField(
            model_name='singup',
            name='image',
            field=models.ImageField(upload_to='profile'),
        ),
    ]
