# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20141204_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='institutionhistory',
            options={'verbose_name_plural': 'Institution Histories'},
        ),
        migrations.AlterField(
            model_name='degree',
            name='field',
            field=models.ForeignKey(to='api.DegreeField'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='language',
            name='level',
            field=models.ForeignKey(to='api.SkillLevel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.ForeignKey(to='api.SkillLevel'),
            preserve_default=True,
        ),
    ]
