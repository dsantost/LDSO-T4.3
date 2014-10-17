# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20141016_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='entry_grade',
            field=models.DecimalField(max_digits=2, decimal_places=1),
        ),
    ]
