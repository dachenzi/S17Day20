# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='business_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='adminhost',
            field=models.ManyToManyField(to='hostmanager.Host'),
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]
