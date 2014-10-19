from api.models import Institution, Degree
from api.serializers import InstitutionSerializer, DegreeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class InstitutionList(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class DegreeList(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer