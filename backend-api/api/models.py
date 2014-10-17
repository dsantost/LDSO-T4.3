from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


#-----------------Institution Data-----------------#

class Institution(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Phone Number')])
    fax = models.CharField(max_length=13, validators=[RegexValidator(regex='^(\+\d{3})?\d{9}$', message='Must have 9 digits (optional prefix)', code='Invalid Fax Number')])
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=8, validators=[RegexValidator(regex='^\d{4}\-\d{3}$', message='Format: XXXX-XXX', code='Invalid Postal Code')])
    city = models.ForeignKey('City')
    category = models.ForeignKey('Category')
    higher_up = models.ForeignKey('Institution', blank=True, null=True)
    students = models.ManyToManyField('Student', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    code = models.IntegerField()
    entry_grade = models.DecimalField(decimal_places=1, max_digits=3)
    institution = models.ForeignKey('Institution')

    def __unicode__(self):
        return self.abbr


class Course(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    description = models.TextField()
    degree = models.ForeignKey('Degree')

    def __unicode__(self):
        return self.abbr


#-----------------Misc Data-----------------#

class City(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


#-----------------User Data-----------------#

class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name


class Commentary(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    institution = models.ForeignKey('Institution')

    def __unicode__(self):
        if len(self.text) < 50:
            return self.text
        return self.text[:50] + "..."