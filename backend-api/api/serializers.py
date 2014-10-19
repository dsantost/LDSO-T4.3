from rest_framework import serializers
from api.models import Institution, Degree
from django.contrib.auth.models import User


class InstitutionSerializer(serializers.ModelSerializer):
    city = serializers.Field(source='city.name')
    category = serializers.Field(source='category.name')
    higher_up = serializers.Field(source='higher_up.abbr')
    students = serializers.RelatedField(many=True)

    class Meta:
        model = Institution
        fields = ('name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'city', 'category', 'higher_up', 'students',)


class DegreeSerializer(serializers.ModelSerializer):
    institution = serializers.RelatedField()

    class Meta:
        model = Degree
        fields = ('name', 'abbr', 'code', 'entry_grade', 'institution')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')