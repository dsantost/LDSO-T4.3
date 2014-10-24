# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20141019_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('degree', models.ForeignKey(to='api.Degree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='commentary',
            options={'verbose_name_plural': 'Commentaries'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='institution',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='institution',
            name='page_color',
            field=models.CharField(default=b'ffffff', max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.ForeignKey(default=0, to='api.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='facebook_link',
            field=models.URLField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='github_link',
            field=models.URLField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='linkedin_link',
            field=models.URLField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='profile_visibility',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='twitter_link',
            field=models.URLField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
