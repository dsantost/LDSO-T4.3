# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_institution_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(related_name='enrollments', to='api.Student'),
            preserve_default=True,
        ),
    ]
