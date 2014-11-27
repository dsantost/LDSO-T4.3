from api import models
from api import serializers
from django.contrib.auth.models import User
from rest_framework import generics


# Institution
class InstitutionList(generics.ListCreateAPIView):
    queryset = models.Institution.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.InstitutionsGETSerializer

        if self.request.method == 'POST':
            return serializers.InstitutionsPOSTSerializer


class InstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Institution.objects.all()
    serializer_class = serializers.InstitutionSerializer


# Degree
class DegreeList(generics.ListCreateAPIView):
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer


class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer


# City
class CityList(generics.ListCreateAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# Company
class CompanyList(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


# Student
class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.StudentGETSerializer

        if self.request.method == 'POST':
            return serializers.StudentPOSTSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentGETSerializer


# Category
class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


# Degree
class DegreeList(generics.ListCreateAPIView):
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer


class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer