from api.models import Institution, Degree, City
from api.serializers import InstitutionSerializer, InstitutionsSerializer, DegreeSerializer, UserSerializer, CitySerializer
from django.contrib.auth.models import User
from rest_framework import generics


class InstitutionList(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionsSerializer


class InstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class DegreeList(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer