from rest_framework import serializers
from api import models
from django.contrib.auth.models import User


# Institution
class InstitutionSerializer(serializers.ModelSerializer):
    city = serializers.Field(source='city.name')
    category = serializers.Field(source='category.name')
    higher_up = serializers.Field(source='higher_up.abbr')
    students = serializers.RelatedField(many=True)

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'city', 'category', 'higher_up', 'students',)


class InstitutionsSerializer(serializers.ModelSerializer):
    category = serializers.Field(source='category.name')

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'category')


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


# Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'name')


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


# EntryGrade
class EntryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryGrade
        fields = ('id', 'year', 'value')


# Degree
class DegreeSerializer(serializers.ModelSerializer):
    institution = serializers.Field(source='institution.name')
    entry_grades = EntryGradeSerializer(many=True)

    class Meta:
        model = models.Degree
        fields = ('id', 'name', 'abbr', 'code', 'institution', 'entry_grades')