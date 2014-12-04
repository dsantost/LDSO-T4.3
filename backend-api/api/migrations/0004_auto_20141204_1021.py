# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141120_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('institution', models.ForeignKey(related_name='histories', to='api.Institution')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(default=b'3', max_length=1, choices=[(b'5', b'Beginner'), (b'4', b'Novice'), (b'3', b'Moderate'), (b'2', b'Proficient'), (b'1', b'Expert')])),
                ('student', models.ForeignKey(related_name='languages', to='api.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(default=b'3', max_length=1, choices=[(b'5', b'Beginner'), (b'4', b'Novice'), (b'3', b'Moderate'), (b'2', b'Proficient'), (b'1', b'Expert')])),
                ('student', models.ForeignKey(related_name='skills', to='api.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='degree',
            name='description',
            field=models.TextField(default=b'', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='degree',
            name='field',
            field=models.CharField(default=b'', max_length=5, choices=[(b'C', b'Ci\xc3\xaancias'), (b'S', b'Sa\xc3\xbade'), (b'T', b'Tecnologias'), (b'ARN', b'Agricultura e Recursos Naturais'), (b'ARPD', b'Arquitetura, Artes Pl\xc3\xa1sticas e Design'), (b'CEFP', b'Ci\xc3\xaancias da Educa\xc3\xa7\xc3\xa3o e Forma\xc3\xa7\xc3\xa3o de Professores'), (b'DCSS', b'Direito, Ci\xc3\xaancias Sociais e Servi\xc3\xa7os'), (b'EGC', b'Economia, Gest\xc3\xa3o e Contabilidade'), (b'HST', b'Humanidades, Secretariado e Tradu\xc3\xa7\xc3\xa3o'), (b'HFDAE', b'Educa\xc3\xa7\xc3\xa3o F\xc3\xadsica, Desporto e Artes do Espet\xc3\xa1culo')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='history_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='presentation',
            field=models.TextField(default=b'', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='presentation_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='students_heading',
            field=models.CharField(default=b'', max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='website_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='wikipedia_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='average',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=b'2000-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='intro',
            field=models.TextField(default=b'', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='credits',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.IntegerField(default=1993),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='facebook_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='github_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='linkedin_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='twitter_link',
            field=models.URLField(default=b'', max_length=150, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
