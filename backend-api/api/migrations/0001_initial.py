# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^(\\+\\d{3})?\\d{9}$', message=b'Must have 9 digits (optional prefix)', code=b'Invalid Phone Number')])),
                ('fax', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^(\\+\\d{3})?\\d{9}$', message=b'Must have 9 digits (optional prefix)', code=b'Invalid Fax Number')])),
                ('address', models.CharField(max_length=200)),
                ('postalcode', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}\\-\\d{3}$', message=b'Format: XXXX-XXX', code=b'Invalid Postal Code')])),
                ('category', models.ForeignKey(to='api.Category')),
                ('city', models.ForeignKey(to='api.City')),
                ('higherup', models.ForeignKey(to='api.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
