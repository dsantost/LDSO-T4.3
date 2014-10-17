# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_course_abbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='higher_up',
            field=models.ForeignKey(blank=True, to='api.Institution', null=True),
        ),
    ]
