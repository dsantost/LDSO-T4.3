# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_entryexam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryexam',
            name='degree',
            field=models.ForeignKey(related_name='entry_exams', to='api.Degree'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='page_color',
            field=models.CharField(default=b'ffffff', max_length=6, blank=True),
            preserve_default=True,
        ),
    ]
