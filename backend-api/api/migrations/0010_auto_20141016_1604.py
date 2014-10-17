# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20141016_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='higher_up',
            field=models.ForeignKey(to='api.Institution', null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='students',
            field=models.ManyToManyField(to=b'api.Student', null=True),
        ),
    ]
