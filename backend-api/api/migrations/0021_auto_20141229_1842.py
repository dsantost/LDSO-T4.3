# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import api.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_institutionadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=api.models.get_file_path)),
                ('degree', models.ForeignKey(related_name='degree_projects', to='api.Degree')),
                ('student', models.ForeignKey(related_name='student_projects', to='api.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='institutionadmin',
            name='institution',
            field=models.ForeignKey(related_name='admins', to='api.Institution'),
            preserve_default=True,
        ),
    ]
