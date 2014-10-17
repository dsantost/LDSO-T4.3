# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20141016_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='abbr',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
