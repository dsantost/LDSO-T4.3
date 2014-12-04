# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20141204_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='history_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='presentation',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='presentation_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='students_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='website_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='institution',
            name='wikipedia_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='facebook_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='github_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='intro',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='linkedin_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='twitter_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
