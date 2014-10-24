# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20141024_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.ForeignKey(blank=True, to='api.City', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='facebook_link',
            field=models.URLField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='github_link',
            field=models.URLField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='linkedin_link',
            field=models.URLField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='twitter_link',
            field=models.URLField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
