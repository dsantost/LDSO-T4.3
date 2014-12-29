# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20141229_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default=b'', max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
