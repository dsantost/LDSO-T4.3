# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_institution_higherup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('institution', models.ForeignKey(to='api.Institution')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
                ('entry_grade', models.IntegerField()),
                ('institution', models.ForeignKey(to='api.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.ForeignKey(to='api.Degree'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='higherup',
            new_name='higher_up',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='postalcode',
            new_name='postal_code',
        ),
        migrations.AddField(
            model_name='institution',
            name='students',
            field=models.ManyToManyField(to='api.Student'),
            preserve_default=True,
        ),
    ]
