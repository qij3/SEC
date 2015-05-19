# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_team_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='project_status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'In Process'), (2, b'Finished')]),
        ),
    ]
