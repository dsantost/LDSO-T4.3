from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


#-----------------Institution Data-----------------#

class Institution(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbr = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Phone Number')])
    fax = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Fax Number')])
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=8, validators=[RegexValidator(regex='^\d{4}\-\d{3}$', message='Format: XXXX-XXX', code='Invalid Postal Code')])
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    page_color = models.CharField(max_length=6, default="ffffff")

    #external relations
    city = models.ForeignKey('City')
    category = models.ForeignKey('Category')
    higher_up = models.ForeignKey('Institution', blank=True, null=True)
    students = models.ManyToManyField('Student', through='Enrollment')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Degree(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    code = models.IntegerField()
    institution = models.ForeignKey('Institution', related_name="degrees")

    def __unicode__(self):
        return self.abbr


class Subject(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    description = models.TextField()
    degree = models.ForeignKey('Degree', related_name="subjects")

    def __unicode__(self):
        return self.abbr


class EntryGrade(models.Model):
    degree = models.ForeignKey('Degree', related_name='entry_grades')
    year = models.IntegerField()
    value = models.FloatField()

    def __unicode__(self):
        return str(self.value)


#-----------------Misc Data-----------------#
class City(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Cities"


#-----------------User Data-----------------#

class Student(models.Model):
    user = models.OneToOneField(User)

    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey('City', blank=True, null=True)

    profile_visibility = models.BooleanField(default=True)
    facebook_link = models.URLField(max_length=150, blank=True, null=True)
    linkedin_link = models.URLField(max_length=150, blank=True, null=True)
    twitter_link = models.URLField(max_length=150, blank=True, null=True)
    github_link = models.URLField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return self.name


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


class Enrollment(models.Model):
    institution = models.ForeignKey('Institution')
    student = models.ForeignKey('Student', related_name='enrollments')
    year = models.IntegerField()
    active = models.BooleanField(default=True)