# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import core.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150520_0509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='working_status',
        ),
        migrations.RemoveField(
            model_name='team',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 5, 20, 23, 58, 22, 715411, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 5, 20, 23, 58, 40, 603303, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='project_status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'MVP - SEEKING ANGEL'), (2, b'SEEKING - A Round'), (3, b'SEEKING - B Round'), (4, b'Others')]),
        ),
    ]
