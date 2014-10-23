from rest_framework import serializers
from api.models import Institution, Degree, City
from django.contrib.auth.models import User


class InstitutionSerializer(serializers.ModelSerializer):
    city = serializers.Field(source='city.name')
    category = serializers.Field(source='category.name')
    higher_up = serializers.Field(source='higher_up.abbr')
    students = serializers.RelatedField(many=True)

    class Meta:
        model = Institution
        fields = ('id', 'name', 'abbr', 'email', 'phone', 'fax', 'address', 'postal_code', 'city', 'category', 'higher_up', 'students',)


class InstitutionsSerializer(serializers.ModelSerializer):
    category = serializers.Field(source='category.name')

    class Meta:
        model = Institution
        fields = ('id', 'name', 'abbr', 'category')


class DegreeSerializer(serializers.ModelSerializer):
    institution = serializers.RelatedField()

    class Meta:
        model = Degree
        fields = ('id', 'name', 'abbr', 'code', 'entry_grade', 'institution')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')