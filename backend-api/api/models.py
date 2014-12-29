# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import uuid
import os
from django.utils.deconstruct import deconstructible


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('avatars', filename)


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

#########################################################################
# Institution
#########################################################################

class Institution(models.Model):
    # Data
    name = models.CharField(max_length=100, unique=True)
    abbr = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Phone Number')])
    fax = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Fax Number')])
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=8, validators=[RegexValidator(regex='^\d{4}\-\d{3}$', message='Format: XXXX-XXX', code='Invalid Postal Code')])
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # View
    page_color = models.CharField(max_length=6, blank=True, default="ffffff")
    presentation_heading = models.CharField(blank=True, max_length=500, default="")
    presentation = models.TextField(blank=True, default="")
    history_heading = models.CharField(blank=True, max_length=500, default="")
    students_heading = models.CharField(blank=True, max_length=500, default="")
    wikipedia_link = models.URLField(max_length=150, blank=True, default="")
    website_link = models.URLField(max_length=150, blank=True, default="")

    # External relations
    city = models.ForeignKey('City')
    category = models.ForeignKey('Category')
    higher_up = models.ForeignKey('Institution', blank=True, null=True)
    students = models.ManyToManyField('Student', through='Enrollment')

    def __unicode__(self):
        return self.name


class InstitutionHistory(models.Model):
    heading = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    content = models.TextField()
    institution = models.ForeignKey('Institution', related_name="histories")

    def __unicode__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Institution Histories"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class DegreeField(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class InstitutionAdmin(models.Model):
    user = models.OneToOneField(User)
    institution = models.ForeignKey('Institution', related_name='admins')

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Institution Admins"

#########################################################################
# Degree
#########################################################################

class Degree(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    code = models.IntegerField()
    description = models.TextField(blank=True, default="")
    field = models.ForeignKey('DegreeField')
    institution = models.ForeignKey('Institution', related_name="degrees")

    def __unicode__(self):
        return self.abbr


class Subject(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="")
    year = models.IntegerField()
    credits = models.IntegerField()
    degree = models.ForeignKey('Degree', related_name="subjects")

    def __unicode__(self):
        return self.abbr


class EntryGrade(models.Model):
    degree = models.ForeignKey('Degree', related_name='entry_grades')
    year = models.IntegerField()
    value = models.FloatField()

    def __unicode__(self):
        return str(self.value)


class EntryExam(models.Model):
    name = models.CharField(max_length=100)
    optional = models.BooleanField(default=False)
    degree = models.ForeignKey('Degree', related_name="entry_exams")

    def __unicode__(self):
        return self.name


#########################################################################
# Student
#########################################################################

class Student(models.Model):
    user = models.OneToOneField(User)

    # Data
    name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    city = models.ForeignKey('City', blank=True, null=True)
    highschool_average = models.FloatField(blank=True, null=True)

    # View
    intro = models.TextField(blank=True, default="")
    profile_visibility = models.BooleanField(default=True)
    facebook_link = models.URLField(max_length=150, blank=True, default="")
    linkedin_link = models.URLField(max_length=150, blank=True, default="")
    twitter_link = models.URLField(max_length=150, blank=True, default="")
    github_link = models.URLField(max_length=150, blank=True, default="")
    avatar = models.ImageField(upload_to=PathAndRename("profiles"))

    def __unicode__(self):
        return self.name


class SkillLevel(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('SkillLevel')
    student = models.ForeignKey('Student', related_name="skills")

    def __unicode__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.ForeignKey('SkillLevel')
    student = models.ForeignKey('Student', related_name="languages")

    def __unicode__(self):
        return self.name


class Enrollment(models.Model):
    institution = models.ForeignKey('Institution')
    degree = models.ForeignKey('Degree')
    student = models.ForeignKey('Student', related_name='enrollments')
    year = models.IntegerField()
    active = models.BooleanField(default=True)


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True, default="")
    degree = models.ForeignKey('Degree', related_name='degree_projects')
    student = models.ForeignKey('Student', related_name='student_projects')
    image = models.ImageField(upload_to=PathAndRename("projects"), blank=True, null=True)
    link = models.URLField(max_length=150, blank=True, default="")

    def __unicode__(self):
        return self.name


#########################################################################
# Company
#########################################################################

class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, related_name='comments')
    institution = models.ForeignKey('Institution', related_name='comments')

    def __unicode__(self):
        if len(self.text) < 50:
            return self.text
        return self.text[:50] + "..."

    class Meta:
        verbose_name_plural = "Comments"


#########################################################################
# Auxiliary
#########################################################################


class City(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Cities"