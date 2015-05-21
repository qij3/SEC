# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150520_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'IT'), (2, b'Finance'), (3, b'Hardware'), (4, b'Bio'), (5, b'Others')]),
        ),
    ]
