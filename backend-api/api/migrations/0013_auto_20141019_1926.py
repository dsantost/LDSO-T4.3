# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_institution_abbr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('degree', models.ForeignKey(to='api.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='course',
            name='degree',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
