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
        fields = ('id', 'institution', 'year', 'active')


# Student
class SkillSerializer(serializers.ModelSerializer):
    level = serializers.Field(source="level.name")

    class Meta:
        model = models.Skill
        fields = ('id', 'name', 'level')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ('id', 'name', 'level')


class StudentGETSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True)
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)

    class Meta:
        model = models.Student
        fields = ('id', 'name', 'birthdate', 'city', 'highschool_average', 'intro', 'profile_visibility', 'facebook_link', 'linkedin_link', 'twitter_link', 'github_link', 'enrollments', 'skills', 'languages')


class StudentPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ('id', 'user', 'name', 'birthdate', 'city', 'facebook_link', 'linkedin_link', 'twitter_link', 'github_link', 'profile_visibility')


# EntryGrade
class EntryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryGrade
        fields = ('id', 'year', 'value')


# Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name', 'abbr', 'description', 'credits')


# Degree
class EntryExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryExam
        fields = ('id', 'name')


class DegreeSerializer(serializers.ModelSerializer):
    institution = serializers.Field(source='institution.name')
    entry_grades = EntryGradeSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    entry_exams = EntryExamsSerializer(many=True)

    class Meta:
        model = models.Degree
        fields = ('id', 'name', 'abbr', 'code', 'description', 'field', 'institution', 'entry_grades', 'entry_exams', 'subjects')


# Institution
class InstitutionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'name')


class InstitutionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstitutionHistory
        fields = ('id', 'heading', 'date', 'content')


class InstitutionSerializer(serializers.ModelSerializer):
    city = serializers.Field(source='city.name')
    category = serializers.Field(source='category.name')
    higher_up = serializers.Field(source='higher_up.abbr')
    students = InstitutionStudentSerializer(many=True)
    degrees = DegreeSerializer(many=True)
    comments = CommentSerializer(many=True)
    histories = InstitutionHistorySerializer(many=True)

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'page_color', 'presentation_heading', 'presentation', 'history_heading', 'students_heading', 'wikipedia_link', 'website_link', 'city', 'category', 'higher_up', 'histories', 'students', 'degrees', 'comments')


class InstitutionsGETSerializer(serializers.ModelSerializer):
    category = serializers.Field(source='category.name')

    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'category')


class InstitutionsPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'page_color', 'city', 'category', 'higher_up')


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