# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20141229_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=api.models.get_file_path, blank=True),
            preserve_default=True,
        ),
    ]
