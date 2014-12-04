# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20141204_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institutionhistory',
            options={'verbose_name_plural': 'Histories'},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='average',
            new_name='highschool_average',
        ),
    ]
