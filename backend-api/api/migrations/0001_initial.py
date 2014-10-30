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
                'verbose_name_plural': 'Categories',
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
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'Comments',
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
                'verbose_name_plural': 'Companies',
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntryGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('degree', models.ForeignKey(related_name='entry_grades', to='api.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('abbr', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^(\\+\\d{3})?\\d{9}$', message=b'Must have 9 digits (optional prefix)', code=b'Invalid Phone Number')])),
                ('fax', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex=b'^(\\+\\d{3})?\\d{9}$', message=b'Must have 9 digits (optional prefix)', code=b'Invalid Fax Number')])),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(regex=b'^\\d{4}\\-\\d{3}$', message=b'Format: XXXX-XXX', code=b'Invalid Postal Code')])),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('page_color', models.CharField(default=b'ffffff', max_length=6)),
                ('category', models.ForeignKey(to='api.Category')),
                ('city', models.ForeignKey(to='api.City')),
                ('higher_up', models.ForeignKey(blank=True, to='api.Institution', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('profile_visibility', models.BooleanField(default=True)),
                ('facebook_link', models.URLField(max_length=150, null=True, blank=True)),
                ('linkedin_link', models.URLField(max_length=150, null=True, blank=True)),
                ('twitter_link', models.URLField(max_length=150, null=True, blank=True)),
                ('github_link', models.URLField(max_length=150, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='api.City', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('abbr', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('degree', models.ForeignKey(related_name='subjects', to='api.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='institution',
            field=models.ForeignKey(to='api.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(to='api.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='degree',
            name='institution',
            field=models.ForeignKey(related_name='degrees', to='api.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='institution',
            field=models.ForeignKey(related_name='comments', to='api.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
