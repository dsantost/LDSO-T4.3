# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20141204_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryExam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('optional', models.BooleanField(default=False)),
                ('degree', models.ForeignKey(related_name='entry_exames', to='api.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
