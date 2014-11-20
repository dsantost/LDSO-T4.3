from rest_framework import serializers
from api import models
from django.contrib.auth.models import User


# Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'user', 'institution', 'pub_date', 'text')


# Enrollment
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = ('id', 'institution', 'student', 'year', 'active')


# Student
class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True)

    class Meta:
        model = models.Student
        fields = ('id', 'name', 'enrollments')


# EntryGrade
class EntryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryGrade
        fields = ('id', 'year', 'value')


# Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name', 'abbr', 'description')


# Degree
class DegreeSerializer(serializers.ModelSerializer):
    institution = serializers.Field(source='institution.name')
    entry_grades = EntryGradeSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = models.Degree
        fields = ('id', 'name', 'abbr', 'code', 'institution', 'entry_grades', 'subjects')


# Institution
class InstitutionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'name')


class InstitutionSerializer(serializers.ModelSerializer):
    city = serializers.Field(source='city.name')
    category = serializers.Field(source='category.name')
    higher_up = serializers.Field(source='higher_up.abbr')
    students = InstitutionStudentSerializer(many=True)
    degrees = DegreeSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'city', 'category', 'higher_up', 'students', 'degrees', 'comments')


class InstitutionsGETSerializer(serializers.ModelSerializer):
    category = serializers.Field(source='category.name')

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'category')


class InstitutionsPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'city', 'category', 'higher_up')


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


# City
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name')


# Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name')


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')