# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20141204_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='degree',
            field=models.ForeignKey(default=1, to='api.Degree'),
            preserve_default=False,
        ),
    ]
