# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='higherup',
        ),
    ]
