# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20141024_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='entry_grade',
        ),
    ]
