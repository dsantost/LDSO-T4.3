# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_student_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='avatar',
        ),
    ]
