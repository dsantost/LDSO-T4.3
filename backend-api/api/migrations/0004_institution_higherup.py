# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_institution_higherup'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='higherup',
            field=models.ForeignKey(default=0, to='api.Institution'),
            preserve_default=False,
        ),
    ]
