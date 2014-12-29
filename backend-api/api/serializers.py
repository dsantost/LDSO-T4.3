from rest_framework import serializers
from api import models
from django.contrib.auth.models import User
from rest_framework.decorators import api_view


#########################################################################
# City
#########################################################################

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name')


#########################################################################
# User
#########################################################################

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


#########################################################################
# Student
#########################################################################

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = ('id', 'institution', 'degree', 'year', 'active')


class SkillSerializer(serializers.ModelSerializer):
    level = serializers.Field(source="level.name")

    class Meta:
        model = models.Skill
        fields = ('id', 'name', 'level')


class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillLevel
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = ('id', 'name', 'level')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'description', 'degree', 'student', 'image', 'link')


class StudentGETSerializer(serializers.ModelSerializer):
    username = serializers.Field(source="user.username")
    email = serializers.Field(source="user.email")
    enrollments = EnrollmentSerializer(many=True)
    skills = SkillSerializer(many=True)
    languages = LanguageSerializer(many=True)
    student_projects = ProjectSerializer(many=True)

    class Meta:
        model = models.Student
        fields = ('id', 'username', 'email', 'name', 'birthdate', 'city', 'highschool_average', 'intro', 'profile_visibility', 'facebook_link', 'linkedin_link', 'twitter_link', 'github_link', 'enrollments', 'skills', 'languages', 'student_projects', 'avatar')


class StudentPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'user', 'name', 'birthdate', 'city', 'facebook_link', 'linkedin_link', 'twitter_link', 'github_link', 'profile_visibility', 'avatar')

#########################################################################
# Company
#########################################################################

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name')


#########################################################################
# Instituion Admins
#########################################################################

class InstitutionAdminSerializer(serializers.ModelSerializer):
    username = serializers.Field(source="user.username")
    email = serializers.Field(source="user.email")

    class Meta:
        model = models.InstitutionAdmin
        fields = ('id', 'username', 'email', 'institution')


#########################################################################
# Degree
#########################################################################

class EntryGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryGrade
        fields = ('id', 'year', 'value')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name', 'abbr', 'description', 'credits')


class EntryExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EntryExam
        fields = ('id', 'name')


class DegreeFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeField
        fields = ('id', 'name')


class DegreeGETSerializer(serializers.ModelSerializer):
    institution = serializers.Field(source='institution.name')
    entry_grades = EntryGradeSerializer(many=True)
    subjects = SubjectSerializer(many=True)
    entry_exams = EntryExamsSerializer(many=True)
    degree_projects = ProjectSerializer(many=True)

    class Meta:
        model = models.Degree
        fields = ('id', 'name', 'abbr', 'code', 'description', 'field', 'institution', 'entry_grades', 'entry_exams', 'subjects', 'degree_projects')


class DegreePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Degree
        fields = ('id', 'name', 'abbr', 'code', 'description', 'field', 'institution')


#########################################################################
# Institution
#########################################################################

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id', 'user', 'institution', 'pub_date', 'text')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


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
    degrees = DegreeGETSerializer(many=True)
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