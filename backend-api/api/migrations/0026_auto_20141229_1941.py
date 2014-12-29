# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20141229_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=api.models.PathAndRename(b'projects'), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(upload_to=api.models.PathAndRename(b'avatars')),
            preserve_default=True,
        ),
    ]
