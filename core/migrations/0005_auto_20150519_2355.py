# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='members',
            field=models.ForeignKey(blank=True, to='core.Team', null=True),
        ),
    ]
